'''
条件判断，循环
'''

# 条件判断简单使用
def conditional():
    name = "蒋蒋"
    # 注意： 非 0 为true，但是 "" 字符串是false，[]，(),{} 空数组和对象包括 None 也是 false
    if name:
        print(f'name有值，name={name}')

    count = 10#int(input("请输入数量: "))

    if count == 10 or count < 10:
        print("count等于10或者小于10")
    elif count > 11 and count < 15:
        print("count大于11并且小于15")
    elif not(count > 15 and count > 20):
        print("count没有大于15也没有大于20（not就是取反的意思）")
    else:
        # pass 用来保证语法编译不出现错误（一般用来标识这个位置还会用来写代码）
        pass
        #print("count不等于10也不等于11")

# 循环简单使用
def circulate():
    print("循环--------------------------------开始")
    count = 10
    while count > 0:
        # end="" 表示输出不换行，其实就是在最后一个字符上不自动加上换行符，而是加上 ""
        print(f'count={count},',end="")
        count-=1

    # 输出一个换行
    print("")

    quantity = 9
    # 注意：python循环数字都是这样写的，如果是循环对象或数组或字符串就不需要range了包装了（注意：range的第三个参数就是每次递增数量，相当于 i加几）
    for i in range(0,quantity,1):
        # continue 跳出单次循环
        if i==5:
            continue
        # break 跳出整个循环
        if i==7:
            break
        print(f'i={i},',end="")

    name="我的名字叫蒋蒋"

    # 输出一个换行
    print("")

    # 循环字符串获取到每一个字符串
    for n in name:
        print(f'n={n}',end="")

    # 打印一个倒三角形（注意：range的第三个参数就是每次递增数量，相当于 i加几）
    for t in range(0,6,1):
        print("")
        # 输出三角形前面的空格
        for y in range(0,t):
            print(" ",end="")
        # 输出星星
        for j in range(1, 6-t):
            print("* ",end="")

if __name__ == '__main__':
    conditional()
    circulate()

