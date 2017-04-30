## 0x00 预览：
![image](https://github.com/0x024/alimemeda/blob/master/data/log/exp.png)

## 0x01环境：
[![](https://img.shields.io/badge/Ubuntu-16.04LTS-brightgreen.svg)]()
[![](https://img.shields.io/badge/Python-2.7-brightgreen.svg)]()
[![](https://img.shields.io/badge/OpenCV-3.2.0-brightgreen.svg)]()

```
curl安装：
	sudo apt-get install curl
```




```
OpenCV 3.2.0
	sudo apt-get install build-essential
	sudo apt-get install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev
	sudo apt-get install python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev
	git clone https://github.com/0x024/opencv.git    #为了方便,我已经将需要的包整合到我的github上，可以直接下载编译，
	cd opencv #进入OpenCV目录
	mkdir release
	cd release
	cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local ..  #如果出现download ippicv失败的信息，重复运行本命令即可，还是不行，请挂代理！
	make -j4  #这里的-j4代表job数，越大编译的速度越快
	sudo make install
```


## 0x02 目录树:

![image](https://github.com/0x024/alimemeda/blob/master/data/log/tree.png)

## 0x03 执行:

```
运行前，

	需要将alimemeda.py中的api_key和api_secret换成你的
	(为了便于您测试,我以将我的key放在里面，为了防止多人使用outer_id冲突，希望您后期换成您自己的)
	需要将所需要识别的截图放在/img目录下，暂时只可识别一张

```





```java
python alimemeda.py  #运行完毕后，会覆盖原有的图片。
```



