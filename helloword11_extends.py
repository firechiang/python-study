'''
继承相关
'''

# 家禽类
class poultry:

    def get_home(self):
        print("回家了")

# 动物类
class animal:
    def __init__(self,name):
        # 两个下划线开头的属性表示是私有的，不允许外部访问，相当于JAVA的 private 修饰（注意：外部要访问建议使用get函数）
        self.__name = name

    def get_name(self):
        return self.__name

# 继承至animal和poultry
class pig(animal,poultry):

    # 猪的颜色
    def __init__(self,name,color):
        # 调用父类的初始化函数
        super(pig, self).__init__(name)
        self.__color = color

    def get_color(self):
        return self.__color

    # toString函数
    def __str__(self):
        return f'pig(name={self.get_name()},color={self.get_color()})'

    # 重写父类的函数
    def get_home(self):
        # 调用父类的函数
        super().get_home()
        print("猪回家了")

if __name__ == "__main__":
    p = pig("猪","黄色")
    print(f"pig={p}")
    p.get_home()