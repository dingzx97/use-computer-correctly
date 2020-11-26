# frp内网穿透

1. 需要准备一台有公网ip的电脑做中介，比如说云服务器；
2. 从[frp的GitHub](https://github.com/fatedier/frp/releases)下载电脑系统对应的文件；
3. 服务器端将frps文件放于/usr/bin/路径下，`frps.ini`、`frps_full.ini`、`frps.service`、`frps@.service`四个文件放于/etc/frp/路径下(没有就创建一个文件夹)，并配置`frps.ini`文件，设置绑定的端口（如果是在云服务器上需要开放相应的端口，frps和frpc用到的端口都需要开放）；
4. 输入`systemctl enable /etc/frp/frps.service`开机自启frps服务;
5. 输入`systemctl start frps`立即启动frps服务;
6. 客户端将frpc文件放于/usr/bin/路径下，`frpc.ini`、`frpc_full.ini`、`frpc.service`、`frpc@.service`四个文件放于/etc/frp/路径下(没有就创建一个文件夹)，并配置`frpc.ini`文件，填写服务器IP地址及端口，根据自己需要配置一下；
7. 输入`systemctl enable /etc/frp/frpc.service`开机自启frpc服务;
8. 输入`systemctl start frpc`立即启动frpc服务。

