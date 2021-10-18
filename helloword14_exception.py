'''
异常处理简单使用
'''

# 自定义异常，继承自 Exception
class CustomException(Exception):
    def __init__(self,msg):
        self.msg = msg

    def __str__(self):
        return f'程序发生自定义异常（msg={self.msg}）'


if __name__ == "__main__":
    # 捕获异常
    try:
        file = open("file","r")
    # 捕获单个异常(注意：Exception是所有异常的父类)
    #except Exception as e:
    # 捕获多个异常
    except (NameError,FileNotFoundError) as e:
        print(f"找不到文件 file e={e}")
    else:
        print("没有异常会执行的代码（这个一般不用）")
    finally:
        print("和JAVA的finally是一个意思")