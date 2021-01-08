# 搭建KSM服务器

使用的是vlmcsd这个软件，[GitHub地址](https://github.com/Wind4/vlmcsd)；

大佬还提供了容器的构建文件，[这里](https://github.com/Wind4/vlmcsd-docker)；

大佬赛高~



KMS服务器网址：kms.dingzx97.cn



我自己搭建的过程：

```bash
git clone --branch master --single-branch https://github.com/Wind4/vlmcsd.git vlmcsd
cd vlmcsd
make
cp bin/vlmcsd /usr/bin/
```

编写服务文件，放在`/lib/systemd/system`路径下面，我起的文件名是`vlmcsd.service`，添加以下内容：

```
[Unit]
Description=vlmcsd server
After=network-online.target

[Service]
ExecStart=/usr/bin/vlmcsd -d -D
ExecReload=/bin/kill -HUP $MAINPID
RestartSec=2
Restart=on-failure

[Install]
WantedBy=multi-user.target  
```

然后执行：

```
systemctl enable vlmcsd
systemctl start vlmcsd
systemctl status vlmcsd
```

应该就可以了，默认使用的是1688端口，用云服务器搭建得开放相应端口。

其实只要下载运行大佬的软件就好，自己简单的学了学怎么写这个服务的文件，也没啥难度。

