'''
Map简单使用
'''

if __name__ == "__main__":
    map = {
        "name": "jiangjian",
        "age": 13
    }
    print(f'name={map}')
    print("---------------------------------")
    for key in map.keys():
        print(f'key={key},value={map[key]}')

    print("---------------------------------")
    for item in map.items():
        print(f'key={item[0]},value={item[1]}')

    print("---------------------------------")
    for value in map.values():
        print(f'value={value}')

    print("---------------------------------")
    # 添加元素 asdasd
    map["asdasd"] = "asdasda"

    print(f'map.name={map.get("name")}')
    print(f'map.name={map["name"]}')
    print(f'map的大小={len(map)}')
    print(f'map里面是否包含name属性={"name" in map}')

    # 删除元素
    del map["name"]
    # 清空 map
    map.clear()
    # 删除整个 map
    del map