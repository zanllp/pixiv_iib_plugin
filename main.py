import os
from scripts.iib.parsers.model import ImageGenerationInfo, ImageGenerationParams
from PIL import Image
import csv
from plugins.pixiv_iib_plugin.path_tree import PathTree
import codecs
import re
from scripts.iib.tool import build_sd_webui_style_img_gen_info, map_dict_keys, omit, replace_punctuation
import json


class Main:
    def __init__(self):
        # These two are required
        self.name = "Pixiv IIB Plugin"
        self.source_identifier = "PixivBatchDownloader"
        # These keys will be converted to tags in the corresponding meta, which you can see on the ImageSearch page
        self.extra_convert_to_tag_meta_keys = ["AI", "Artist", "type", "Artist User Id"]
        self.img_infos = {}
        self.dir_csv_reached_tree = PathTree()

    # This function is required
    def parse(self, img: Image, file_path):
        file_path = self.convert_p0(file_path)
        if not self.test(img, file_path):
            raise Exception("The input image does not match the current parser.")
        imgdata = self.img_infos.get(file_path)
        prompt = imgdata.get("tags_transl") or imgdata.get("tags")
        meta_raw = omit(
            map_dict_keys(imgdata, {"user": "Artist", "userId": "Artist User Id"}),
            ["fileName", "page", "title"],
        )

        # 'steps' is a workaround
        meta = {
            "Steps": "Unknown",
            "title": imgdata.get("title") or "Unknown",
            "description": imgdata.get("description") or "Unknown",
            **meta_raw,
            "tags": json.dumps(meta_raw["tags"], ensure_ascii=False),
            "tags_transl": json.dumps(meta_raw["tags_transl"], ensure_ascii=False),
            "Source Identifier": self.source_identifier,
        }

        for key in meta:
            if key not in ["tags", "tags_transl", "Source Identifier"]:
                meta[key] = replace_punctuation(meta[key])  

        info = build_sd_webui_style_img_gen_info(
            prompt=prompt,
            meta=meta,
        )
        return ImageGenerationInfo(
            info,
            ImageGenerationParams(
                meta=meta,
                pos_prompt=map(lambda x: x.strip(), prompt.split(",")),
            ),
        )

    # This function is used to determine if the image belongs to this plugin, returning True or False. This function is required.
    def test(self, img: Image, file_path: str):
        try:
            file_path = self.convert_p0(file_path)
            if self.img_infos.get(file_path) is None:
                self.init_img_info_from_top_to_bottom(file_path)

            r = self.img_infos.get(file_path)
            return bool(r)
        except Exception as e:
            return False

    def convert_p0(self, file_path: str):
        return re.sub(r"p[0-9]+\.", "p0.", file_path)

    def init_img_info_from_top_to_bottom(self, img_path: str):
        if self.img_infos.get(img_path) is not None:
            return
        curr_dir = os.path.dirname(img_path)
        frags = curr_dir.split(os.path.sep)
        while len(frags) > 1:  # ignore root
            frags.pop()
            self.init_img_info_from_csv_dir(curr_dir)
            curr_dir = os.path.dirname(curr_dir)

    def check_csv_is_valid(self, csv_file: str):
        required_fields = set(
            [
                "id",
                "tags",
                "tags_transl",
                "title",
                "description",
                "date",
                "original",
                "thumb",
                "fileName",
            ]
        )
        with codecs.open(csv_file, "r", "utf-8-sig") as f:
            fl = f.readline().strip()
            flset = fl.split(",")
            return required_fields.issubset(set(flset))

    def init_img_info_from_csv_dir(self, csv_dir: str):
        # Pruning
        if self.dir_csv_reached_tree.get(csv_dir) is not None:
            return
        csvs = []
        for filename in os.listdir(csv_dir):
            if filename.endswith(".csv"):
                csvs.append(os.path.join(csv_dir, filename))
        if len(csvs) == 0:
            return
        for csv_file in csvs:
            if not self.check_csv_is_valid(csv_file):
                continue
            with codecs.open(csv_file, "r", "utf-8-sig") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    abs_path = os.path.normpath(os.path.join(csv_dir, row["fileName"]))
                    self.img_infos[abs_path] = row

        self.dir_csv_reached_tree.insert(csv_dir, True)