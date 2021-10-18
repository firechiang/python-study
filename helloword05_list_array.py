'''
数组和集合简单使用
'''

if __name__ == "__main__":
    names = ["maomoa","tata","wenjua"]
    names2 = ["1","3"]

    set1 = {1,2,3}
    # 将一个set集合转换为list
    list = list(set1)
    print(f'list={list}')

    # 用for循环生成一个数组，每次循环取ss的值放到数组里面
    ints = [ ss for ss in range(1,10)]
    print(f'ints={ints}')

    # 用for循环生成一个数组，每次循环如果ss的值是基数就将ss的值放到数组里面
    ints1 = [ ss for ss in range(1,10) if ss % 2 == 1]
    print(f'ints1={ints1}')

    # 用for循环生成一个数组，每次循环（注意：这里说的是第二个循环，还有第二个循环是嵌套在第一个循环里面的）取xx的值放到数组里面
    # 执行过程：当xx=0时，第二个循环每循环一次（一轮循环4次，0-4嘛）将xx的值放入数组，第一轮循环完成 数组里面会有4个0。第二轮循环完成 数组里面会有4个1。最后得到 [0, 0, 0, 0, 1, 1, 1, 1]
    longs = [xx for xx in range(0,2) for yy in range(0,4)]
    print(f'longs={longs}')

    # 注意：range的第三个参数就是每次递增数量，相当于 i加几
    ffffs = [[ff,ff+1,ff+2] for ff in range(1,100,3)]
    print(f'ffffs={ffffs}')

    for i,item in enumerate(names2):
        print(f'i={i},value={item}')

    # 添加元素
    names.append("aaaa")
    # 将字符串AAA的每一个字符插入到数组 names
    names+="AAA"

    # 在3号位插入元素 "2"
    names.insert(2,"2")
    # 修改元素的值
    names[1] = "sdas"
    print(f'names={names}')

    # 将names2里面的所有元素添加到names里面
    names.extend(names2)

    print(f'names的长度={len(names)}')
    print(f'names的第一个元素={names[0]}')
    print(f'names里面aaa出现的次数={names.count("aaa")}')
    print(f'names里面是否包含aaa={"aaa" in names}')
    print(f'names里面是否不包含aaa={"aaa" not in names}')
    # 删除数组里面的最后一个元素，并返回
    aaa = names.pop()
    # 删除指定元素，如果没有则报错
    names.remove("aaaa")
    # 将数组反转
    names.reverse()
    # 将数组反转
    names[-1::-1]
    # 排序（reverse=False表示降序,注意： 如果数组里面的元素类型不一样排序时将会报错
    names.sort(reverse=False)

    # 删除元素
    del names[1]
    # 删除整个数组
    del names