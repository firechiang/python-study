#### Centos安装Python3
```bash
# 安装编译相关
$ yum install gcc zlib-devel -y
# 创建并定位到python3源码编译目录
$ mkdir -p /usr/local/python3 && cd /usr/local/python3
$ 下载python3源码
$ wget https://www.python.org/ftp/python/3.8.9/Python-3.8.9.tar.xz
# 解压源码
$ tar -xvf Python-3.8.9.tar.xz
$ cd Python-3.8.9
# 验证编译环境并配置安装目录
$ ./configure --prefix=/usr/local/python3
# 编译安装
$ make && make install
# 创建软连接（以后要使用python3直接使用命令python3即可，要安装依赖使用pip3）
$ ln -s /usr/local/python3/bin/python3 /usr/bin/python3
$ ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3
```
