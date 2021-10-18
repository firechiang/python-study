from distutils.core import setup

setup(name="test_package",version="0.0.1",description="测试打包",author="作者",py_modules=["string_utils"])

'''
打包过程（注意：项目要打包，必须得有setup.py文件，且代码如上）：
1，到该目录下
2，执行命令 python setup.py build 生成build文件
3，执行命令 python setup.py sdist 生成压缩包，压缩包在dist目录下，至此打包完成
4，如果想将该包，安装到本机（就是把它变成系统模块，其它项目可以直接引用），只需要执行命令 python setup.py install 即可
'''