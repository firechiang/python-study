'''
简单工厂模式简单使用
'''

# 创建动物类(注意：所有类默认是从object继承的)
class animal:

    def get_name(self):
       return "我是动物"

# 继承至动物 animal
class pig(animal):

    # 重写父类的函数
    def get_name(self):
       return "我是猪"

# 继承至动物 animal
class dog(animal):

    # 重写父类的函数
    def get_name(self):
       return "我是狗"

# 动物生产者
class factory:

    # 工厂函数
    # 静态函数（注意：静态函数需要带 @classmethod 注解，默认参数是 cls 代表当前类）
    @classmethod
    def create_animal(cls,type):
        if type == "pig":
            return pig()
        if type == "dog":
            return dog()
        return animal()



if __name__ == "__main__":
    pig = factory.create_animal("pig").get_name()
    dog = factory.create_animal("dog").get_name()
    print(f'pig={pig},dog={dog}')
