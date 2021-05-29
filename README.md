# ozaki-ndn

尾崎君のアプリを実行するためにはまず3つのプログラム: ndn-css、NFD、Consumer/ProducerAPI を各コンピュータにインストールする必要があります。

1. ndn-cxx

ndn-cxxをインストールするためには以下を実行する。

```
sudo apt install g++ pkg-config python3-minimal libboost-all-dev libssl-dev libsqlite3-dev

cd ndn-cxx-FCv2
./waf configure
./waf
sudo ./waf install
sudo ldconfig
```

2. NFD

NFDをインストールするためには以下を実行する。

```
sudo apt install libpcap-dev libsystemd-dev

cd NFD-FC
./waf configure  # on CentOS, add --without-pch
./waf
sudo ./waf install
sudo ldconfig
```

3. Consumer/Producer API

Consumer/Producer APIをインストールするには以下を実行する。
```
cd Consumer-Producer-API
./waf configure
./waf
sudo ./waf install
sudo ldconfig
```


その後、尾崎君ドキュメントに従ってnfdを起動しする。その後ndn-skeleton-apps/ndn-cxx-wafにあるconsumer、producer、functionを起動する

docker run -tid --name yolo -p 33115:33115 yoheimmtw/yolo /bin/bash
