'''
字符串相关常用方法
'''

if __name__ == '__main__':
    str1 = "a1010"
    str2 = "ab"
    str3 = str1 + str2
    print(f'str3={str3}')
    print(f'str3的长度={len(str3)}')
    print(f'str3第三个字符={str3[2]}')

    # 注意：取字符串后面的字符可以从-1开始
    print(f'str3的最后一个字符={str3[-1]}')
    print(f'str3第一到第三个字符={str3[0:3]}')

    print(f'str3第二个字符到最后一个字符={str3[1:len(str3)]}')
    # 注意：省略了最后一个字符串的位置，默认就是最后一个字符的位置
    print(f'str3第二个字符到最后一个字符={str3[1:]}')
    print(f'str3第二个字符到最后一个字符={str3[1]}')

    # 注意：截取字符串的话 -1 表示倒数第二个字符串
    print(f'str3第二个字符到倒数第二个字符={str3[1:-1]}')

    # 注意：省略了最后一个字符串的位置，默认就是最后一个字符的位置（注意：2 表示步长，就是每隔几个字符截取一个字符）
    print(f'str3每隔一个字符截取一个={str3[1::2]}')

    # 注意：截取字符串的话 -1 表示倒数第二个字符串（注意：2 表示步长，就是每隔几个字符截取一个字符）
    print(f'str3从0开始到倒数第二个字符每隔一个字符截取一个={str3[1:-1:2]}')
    # 从-1（就是最后一个字符）开始截取，一直到第一个字符，每减一个字符截取一个
    print(f'翻转字符串str3={str3[-1::-1]}')

    # 找不到返回-1
    print(f'字符串1在str3中从左边开始出现的第一个位置={str3.find("1")}')
    print(f'字符串1在str3中从右边开始出现的第一个位置={str3.rfind("1")}')

    # 找不到报错
    print(f'字符串1在str3中从左边开始出现的第一个位置={str3.index("1")}')
    print(f'字符串1在str3中从右边开始出现的第一个位置={str3.rindex("1")}')


    print(f'str3中1字符出现的次数={str3.count("1")}')

    print(f'将str3字符中的1字符替换成2={str3.replace("1","2")}')

   # 切割后隔开符不要（注意：如果不指定隔开符，默认会将空格，换行等符号全部隔开）
    print(f'将字符串str3按照1切割成一个数组={str3.split("1")}')
    print(f'将字符串str3按照换行符切割成一个数组={str3.splitlines()}')

    # 切割后隔开符存在数组中
    print(f'将字符串str3按照1切割成一个数组={str3.partition("1")}')

    print(f'str3首字母大写={str3.capitalize()}')

    print(f'str3全部大写={str3.upper()}')
    print(f'str3全部小写={str3.lower()}')

    print(f'str3在10字符内左对齐=\n{str3.ljust(10)}')
    print(f'str3在10字符内右对齐=\n{str3.rjust(10)}')
    print(f'str3在10字符内居中对齐=\n{str3.center(10)}')

    print(f'str3去除左右两边的空格={str3.strip()}')
    print(f'str3去除左边的空格={str3.lstrip()}')
    print(f'str3去除右边的空格={str3.rstrip()}')

    print(f'str3是否只包含数字={str3.isdigit()}')

    names=["100","200","300"]
    # 这个有点像java的String.join(",","a","b")
    print(f'将一个字符串数组链起来组成一个新的字符串names={",".join(names)}')

