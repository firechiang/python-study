'''
set集合简单使用（没有下标，没有顺序，不允许重复）
'''

if __name__ == "__main__":
    # 定义一个set集合
    set1 = {1,2,3,4}
    # 定义一个空set
    set2 = ()
    # 添加元素
    set1.add(5)
    # 删除并拿出一个元素
    set1.pop()
    # 删除指定元素
    set1.remove(4)
    print(f"set1={set1}")

    list = [1,2,3]
    # 将一个数组转换为set
    set3 = set(list)