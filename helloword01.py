# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

'''
1，获取变量类型
2，字符串格式化输出
3，格式化小数位
'''
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a = 8
    # 注意：Boolean类型首字母要大写
    b = True
    # None表示None空值
    c = None
    name = '蒋蒋'
    print(f'name是不是String类型={isinstance(name,str)}')
    print(f'name是不是Int类型或String类型={isinstance(name,(int,str))}')

    a=1
    b=2
    # 两个值最简单的交换方式
    a,b=b,a
    print(f'a和b交换后结果，a={a},b={b}')

    if not isinstance(a,str):
        print("a不是字符串类型")

    # type()函数用于获取变量类型
    print(type(a))
    print('a.type='+type(a).__name__+',b.type='+type(b).__name__)
    print('1','2','3')
    print(f'a={a},aa={1}')
    # %d表示要获取一个数字，%a表示传入数字a
    print('a=%d'%a)
    print('a=%d'%(a+1))
    print('age=%d,name=%s'%(a,name))
    # %4d 表示要获取一个数字，4 表示会显示4位，如果不够4位就用空格来填充
    print('a=%4d'%a)
    # %04d 表示要获取一个数字，04 表示会显示4位，如果不够4位就用0来填充
    print('a=%04d'%a)
    # %.2f 表示要获取一个浮点数字，.2表示精确到小数点2位
    print('a=%.2f'%a)
    # 两个%%表示要输出一个%，第一个%表示转义
    print('a=%d%%'%a)
    # 输出5个等号
    print("="*5)
    print_hi('测试程序代码')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
