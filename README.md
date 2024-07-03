# pixiv_iib_plugin
 # Preview

可以在bilibili看视频，只有中文版 https://www.bilibili.com/video/BV1qb421n7ih/

you can watch the video on bilibili, only Chinese version https://www.bilibili.com/video/BV1qb421n7ih/


![image](https://github.com/zanllp/pixiv_iib_plugin/assets/25872019/6394e5dd-3ce7-471d-a340-821450a65390)


![image](https://github.com/zanllp/pixiv_iib_plugin/assets/25872019/16404639-1f36-48b4-a7a9-4a15abd91d01)


![image](https://github.com/xuejianxianzun/PixivBatchDownloader/assets/25872019/130c19e6-eb5d-4032-b2ba-79f34d937217)

# how to use
1. install the plugin / 安装插件
```shell
cd /path/to/your/iib/plugins # to the plugins directory of iib, 到iib的插件目录
git clone https://github.com/zanllp/pixiv_iib_plugin
cd ../ # return to the root directory of iib，返回iib的根目录
python app.py
```
2. open the browser and visit iib / 打开浏览器访问iib

添加一个图片所在的文件夹到IIB

add the folder where the images are to IIB
<img width="1448" alt="image" src="https://github.com/zanllp/sd-webui-infinite-image-browsing/assets/25872019/d93dcffd-414a-4006-a0cd-f18a70cbd8ed">

请确保所在的文件夹有PixivBatchDownloader导出的csv文件，并且csv文件里面的路径与实际图片是一样匹配的。IIB将会读取所有的csv文件并逐一匹配获取信息


please make sure the folder contains the csv file exported by PixivBatchDownloader, and the path in the csv file matches the actual image. IIB will read all the csv files and match the information one by one


![image](https://github.com/zanllp/sd-webui-infinite-image-browsing/assets/25872019/01e9594e-977f-486b-a4db-720c4ca58a8a)

<img width="532" alt="image" src="https://github.com/zanllp/pixiv_iib_plugin/assets/25872019/b3409a4e-ed83-473a-bae4-09109a145acc">


# 已知的问题 Known issues

在运行IIB期间向搜索路径内添加图片会导致IIB无法正常工作，这是因为IIB会在启动时读取所有的csv文件，如果在运行期间添加了新的图片，IIB无法感知到这些新的图片。如果需要添加新的图片，需要重启IIB

Adding images to the search path during the operation of IIB will cause IIB to not work properly. This is because IIB reads all csv files when it starts. If new images are added during the operation, IIB cannot sense these new images. If you need to add new images, you need to restart IIB
