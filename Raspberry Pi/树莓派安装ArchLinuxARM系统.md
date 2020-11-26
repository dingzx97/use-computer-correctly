# 安装ArchLnuxARM步骤（３B+、４B）

1. 从网站上下载好**ArchLinuxARM**的系统压缩包，这里就挂个[清华镜像站](https://mirrors.tuna.tsinghua.edu.cn/archlinuxarm/os/)的，下载相应版本的系统；
2. 将SD卡插入读卡器，读卡器接电脑，用Linux系统进行分区，先输入`fdisk -l`看看有没有识别出SD卡；
3. 输入`fdisk /dev/sd*`开始分区，`sd*`是第一步骤里看到的，大概应该是sdb，具体还得看实际是什么，下面的命令中也都需要把`sd*`修改成实际的；
4. 输入以下命令进行分区（就懒得翻译了），按`m`可以查看帮助，跟着下面按就好：

  - Type `o`. This will clear out any partitions on the drive.

  - Type `p` to list partitions. There should be no partitions left.
  - Type `n`, then `p` for primary, `1` for the first partition on the drive, press `ENTER` to accept the default first sector, then type `+200M` for the last sector.（启动分区大小不要小于200M就好）
  - Type `t`, then `c` to set the first partition to type W95 FAT32 (LBA).
  - Type `n`, then `p` for primary, `2` for the second partition on the drive, and then press `ENTER twice` to accept the default first and last sector.
  - Write the partition table and exit by typing `w`.
5. 输入`mkfs.vfat /dev/sd*1`和`mkfs.ext4 /dev/sd*2`格式化分区；
6. 输入`mount /dev/sd*2 /mnt`、`mkdir /mnt/boot`和`mount /dev/sd*1 /mnt/boot`挂在分区，我这样挂在需要注意挂在顺序，先2后1；
7. 输入`tar -zxf ArchLinuxARM-rpi-aarch64-latest.tar.gz -C /mnt`将ArchLinuxARM系统文件解压到SD卡中；
8. 官网说树莓派4在卸载前需要输入`sed -i 's/mmcblk0/mmcblk1/g' root/etc/fstab`命令，来更新其他SD块？这里的/root/etc/fstab路径应该指代的是解压后ArchLinuxARM系统文件里的/etc/fstab，所以按我这个挂载应该输入`sed -i 's/mmcblk0/mmcblk1/g' /mnt/etc/fstab`即可；
9. 输入`umount /mnt/boot`和`umount /mnt`卸载SD卡；
10. 其他，解压完应该就能用了，但在卸载前可以进行一些其他工作方便使用，主要还是设置清华镜像站（`Server = https://mirrors.tuna.tsinghua.edu.cn/archlinuxarm/$arch/$repo`）。修改/etc/pacman.d/mirrorlist（挂在的时候路径是/mnt/etc/pacman.d/mirrorlist）文件，注释掉别的服务器，把清华的网址添加进去；
11. 开始使用，默认用户“alarm”还有“root”,账号同密码。首先输入`pacman-key --init`密钥初始化以及`pacman-key --populate archlinuxarm`添加ArchLinuxARM密钥。
