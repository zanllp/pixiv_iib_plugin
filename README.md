# pixiv_iib_plugin
 # Preview
![image](https://github.com/zanllp/pixiv_iib_plugin/assets/25872019/6394e5dd-3ce7-471d-a340-821450a65390)
![image](https://github.com/zanllp/pixiv_iib_plugin/assets/25872019/16404639-1f36-48b4-a7a9-4a15abd91d01)


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
