'''
单立设计模式第二种写法简单使用（该写法是通过保证构造器 __new__ 函数只会调用一次，来实现单立）
'''

# 创建类(注意：所有类默认是从object继承的)
class User:

    # 定义一个私有的静态成员变量
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self,name):
        # 两个下划线开头的属性表示是私有的，不允许外部访问，相当于JAVA的 private 修饰（注意：外部要访问建议使用get函数）
        self.__name = name


    def get_name(self):
        return self.__name


if __name__ == "__main__":
    u1 = User("maomoa")
    u2 = User("tianti")
    print(f'user={u1}')
    print(f'user={u1}')
    print("看看两个对象的内存地址是不是相同的")