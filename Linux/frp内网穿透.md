# frp内网穿透

1. 需要准备一台有公网ip的电脑做中介，比如说云服务器；

2. 从[frp的GitHub](https://github.com/fatedier/frp/releases)下载电脑系统对应的文件；

3. 服务端输入命令下载:`wget https://github.com/fatedier/frp/releases/download/v0.34.3/frp_0.34.3_linux_amd64.tar.gz`（也可以自己下好在传到服务器里），之后输入`tar zxvf frp_0.34.3_linux_amd64.tar.gz`解压，输入`cd frp_0.34.3_linux_amd64`进入文件夹；

4. 输入`nano frps.ini`编辑服务端配置文件，设置服务端绑定的端口，默认是7000（如果是在云服务器上需要开放相应的端口，frps和frpc用到的端口都需要开放），也可以再添加个token：

   ```ini
   [common]
   # 设置服务端的端口
   bind_port = 7000
   # 设置客户端连接时使用的token，这个不是必需要设置的
   token = 123456
   ```

5. 将`frps`文件放到/usr/bin/路径下，`frps.ini`和`frps_full.ini`文件放到/etc/frp/路径下(没有就创建一个文件夹)，systemd文件夹下的`frps.service`和`frps@.service`文件放到/usr/lib/systemd/system/路径下，执行以下命令：

   ```bash
   cp frps /usr/bin/
   mkdir -p /etc/frp/
   cp frps.ini /etc/frp/
   cp frps_full.ini /etc/frp/
   mkdir -p /usr/lib/systemd/system/
   cp systemd/frps.service /usr/lib/systemd/system/
   cp systemd/frps@.service /usr/lib/systemd/system/
   ```

6. 输入`systemctl enable frps`开机自启frps服务，输入`systemctl start frps`立即启动frps服务;

7. 客户端下载相应的系统文件，解压后进入文件夹，然后输入`nano frpc.ini`编辑客户端配置文件，设置服务端的ip和端口，还有客户端使用的端口：

   ```ini
   [common]
   # 改成服务端的公网ip
   server_addr = 127.0.0.1
   # 改成服务器的端口
   server_port = 7000
   # 服务器token
   token = 123456
   
   [ssh]
   type = tcp
   local_ip = 127.0.0.1
   local_port = 22
   # 设置客户端使用的端口
   remote_port = 6000
   ```

8. 将`frpc`到/usr/bin/路径下，`frpc.ini`和`frpc_full.ini`文件放到/etc/frp/路径下(没有就创建一个文件夹)，systemd文件夹下的`frpc.service`和`frpc@.service`文件放到/usr/lib/systemd/system/路径下，执行以下命令：

   ```bash
   cp frpc /usr/bin/
   mkdir -p /etc/frp/
   cp frpc.ini /etc/frp/
   cp frpc_full.ini /etc/frp/
   mkdir -p /usr/lib/systemd/system/
   cp systemd/frpc.service /usr/lib/systemd/system/
   cp systemd/frpc@.service /usr/lib/systemd/system/
   ```

9. 输入`systemctl enable frpc`开机自启frpc服务，输入`systemctl start frpc`立即启动frpc服务;

10. 最后，假设服务端公网ip是1.2.3.4，客户端设置的端口是6000，如果其他电脑想要ssh连接客户端，就连接`ssh -p 6000 username@1.2.3.4`即可。

