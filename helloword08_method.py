'''
函数相关（包括lambda表达式函数，和动态代码）简单使用
'''

a = 1

map = {"a":1,"b":2}

# 无返回值的函数
def print_h():
    # 修改全局变量（注意：一定是先写一个 global '变量名'，再在下面一行修改其值。这是一个固定写法）
    global a
    a = 2
    print("测试函数")

# 有参数的函数
def print_i(i):
    map = {"c":3}
    print(f'i={i}')

# 有返回值的函数(直接写return就有返回值)
def sum_(a,b):
    sum = a + b
    map["c"] = 3
    return sum

# 一个函数返回多个
def res(a,b):
    return a,b

# n个参数的传递（注意：*args就相当于java的... 我们接收时它就是元组类型）
def bbb(x,y,*args):
    print(f'x={x},y={y},args={args}')

# n个参数的传递（注意：**args就相当于java的... 不过它是map类型）
def ccc(x, y, **args):
    print(f'x={x},y={y},args={args}')

# 有默认参数值的函数
def aaa(x,a = 1,b=False):
    print(f'x={x},a={a},b={b}')

def ddd(a,b):
    a.replace("a","b")
    b.append("W")

# 匿名函数（lambda表达式函数）
def fff(a,func):

    return func(a)


if __name__ == "__main__":
    print_h()
    print_i(12)
    print(f'1+1={sum_(1,1)}')
    print(f'a={a}')
    print(f'map={map}')

    # 接收多个返回值（注意：该函数需要有多个返回值，才能这样写）
    x,y = res(1,2)
    print(f'x={x},y={y}')
    # 使用单个变量接收多个返回值，那这单个变量就是元组类型
    xy = res(3,4)
    print(f'xy={xy}')

    aaa(1)
    aaa(1,3,True)

    bbb(1,2,10,"aasa")

    # n个参数的传递（注意：**args就相当于java的... 不过它是map类型）
    ccc(1,2,name="jiangjiang",age=22)

    a = "asdasdada"
    b = []
    ddd(a,b)
    print(f'a={a},b={b}')

    # 匿名函数简单使用（lamdba表达式）
    # 定义一个匿名函数
    func = lambda x,y: x+y

    print(f'匿名函数func执行的结果={func(1,1)}')
    # 调用函数fff并传入lambda表达式函数
    val = fff(1,lambda x:x+10)
    print(f'val={val}')

    # 使用lambda表达式匿名函数来自定义排序
    names=[{"name":"maomao","age":62},{"name":"tiantian","age":22}]
    # 根据name排序（注意：reverse=False表示倒序排列）
    names.sort(key=lambda x:x["name"],reverse=False)
    print(f'names排序后的值={names}')
    # 根据age排序
    names.sort(key=lambda age:age["age"])
    print(f'names排序后的值={names}')

    # 动态执行代码
    la = "lambda x,y:x+y"
    # 将字符串转换为代码
    funcc = eval(la)
    print(f'funcc调用结果={funcc(3,5)}')




