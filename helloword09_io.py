'''
file文件简单操作
文件打开模式：
r 只读(默认就是只读)
w 打开一个文件用于覆盖写，如果该文件存在则将其覆盖，不存在就创建文件
a 打开一个文件用于追加写，如果文件存在就在末尾追加写入，如果不存在就创建文件

r+ 打开一个文件用于头部读写，从文件的头部开始进行读写
w+ 打开一个文件用于覆盖读写，如果该文件已存在将其覆盖，如果不存在就创建新文件
a+ 打开一个文件用于追加读写，如果文件存在就在其末尾追加，如果不存在就创建新文件写入

rb 以二进制的方式打开文件用于头部只读，文件的指针将会放在文件的开头（默认模式）
wb 以二进制的方式打开文件用于覆盖写，如果该文件存在将其覆盖，不存在，创建新的文件
ab 以二进制的方式打开文件用于追加写，如果文件存在就在其末尾追加，如果不存在就创建新文件写入

rb+ 以二进制方式打开一个文件用于头部读写，从文件的头部开始进行读写
wb+ 以二进制方式打开一个文件用于覆盖读写，如果该文件已存在将其覆盖，如果不存在就创建新文件
ab+ 以二进制方式打开一个文件用于追加读写，如果文件存在就在其末尾追加，如果不存在就创建新文件写入
'''


import os

if __name__ == "__main__":
    # 打开文件流（os.getcwd()获取当前项目地址）
    file = open("files/aaa.txt",'r')
    print(f'文件相对路径={file.name}')
    print(f'当前目录下files的绝对路劲={os.path.abspath("files")}')
    files_path = os.path.join(os.getcwd(), "files")
    print(f'拼接路径={files_path}')
    print(f'files文件夹的绝对路劲的文件名={os.path.basename(files_path)}')
    print(f'files_path是不是一个文件夹={os.path.isdir(files_path)}')
    print(f'files_path是不是一个文件={os.path.isfile(files_path)}')
    print(f'file文件5个字节的内容={file.read(5)}')
    print(f'file文件的一行内容={file.readline()}')

    print(f'aaa.txt文件大小={os.path.getsize(os.getcwd()+"/files/aaa.txt")}')
    print(f'获取到当前文件读写游标的位置={file.tell()}')
    print(f'当前目录下的所有文件和文件夹={os.listdir()}')
    print(f'当前项目files文件夹下所有文件={os.listdir("files/")}')
    # 修改文件名
    #os.rename("原文件名","新文件名")

    # 重置文件读写游标位置
    # offset 重置位置
    # from   方向（0 文件开头，1 当前位置，2 文件末尾）
    file.seek(0,0)

    while True:
        # 读取一行
        line = file.readline()
        print(line)
        # 如果已经没有数据了跳出循环
        if not line:
            break

    # 重置文件读写游标位置
    file.seek(0, 0)

    print(f'file文件的所有内容={file.read()}')
    # 关闭文件流
    file.close()

    # 拷贝文件
    source_file = open(os.getcwd() + "/files/aaa.txt", 'r')
    target_file = open(os.getcwd()+"/files/aaa2.txt",'w')
    # 原文件内容
    source_content = source_file.read()
    # 将内容写入目标文件
    target_file.write(source_content)
    # 关闭文件流
    source_file.close()
    target_file.close()
