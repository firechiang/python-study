'''
单立设计模式简单使用
'''

# 创建类(注意：所有类默认是从object继承的)
class User:

    # 定义一个私有的静态成员变量
    __instance = None

    def __init__(self,name):
        # 两个下划线开头的属性表示是私有的，不允许外部访问，相当于JAVA的 private 修饰（注意：外部要访问建议使用get函数）
        self.__name = name

    def get_name(self):
        return self.__name

    @classmethod
    def get_instance1(cls):
        # 如果 __instance属性等于 None
        if not cls.__instance:
            # 初始化属性的值
            cls.__instance = User("maomoa")
        return cls.__instance

if __name__ == "__main__":
    u1 = User.get_instance1()
    print(f'user={u1}')