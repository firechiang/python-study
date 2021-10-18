'''
面向对象相关
'''

import random

# 创建类(注意：所有类默认是从object继承的)
class Dice:

    aaa = "公共的静态成员变量"

    # 两个下划线开头的属性表示是私有的，不允许外部访问，相当于JAVA的 private 修饰
    __aaa = "私有的静态成员变量"

    # 静态函数（注意：静态函数需要带 @classmethod 注解，默认参数是 cls 代表当前类）
    @classmethod
    def static_method(cls):
        pass

    # 构造器(注意：该函数一定要返回一个当前类的对象)
    # cls 代表当前类
    def __new__(cls, *args, **kwargs):
        print("对象被构建了")
        #return object.__new__(cls)
        # 这个写法和上面的一样就是构造一个当前类的对象
        return super().__new__(cls)

    # 对象初始化（注意：该函数在构造器后自动调用）
    def __init__(self,count):
        # 两个下划线开头的属性表示是私有的，不允许外部访问，相当于JAVA的 private 修饰（注意：外部要访问建议使用get函数）
        self.__count = count
        print("对象初始化")

    # 对象被销毁时自动调用（注意：只要还有引用指向它，对象就不会被销毁）
    def __del__(self):
        print("该对象内存被释放了")

    # 两个下划线开头的函数表示是私有的不允许外部调用（相当于JAVA的 private 修饰）
    def __aaa(self):
        pass

    def get_count(self):
       return self.__count

    def move(self):
        # 1到7的随机数
        self.__count = random.randint(1,7)

    # ToString函数
    def __str__(self):
        return f'Dice(count={self.__count})'

if __name__ == "__main__":
    # 创建对象
    game = Dice(10)
    print(f'game={game}')
    game.name = "maomoa"
    print(f'game.name={game.name}')
    # 删除属性
    #del game.name
    print(f'game.name={game.name}')