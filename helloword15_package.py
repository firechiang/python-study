'''
package 包相关简单使用
'''

# 导入模块random并取个别名ran
import random as ran
# 直接引入random模块下的randint函数（相当与JAVA的静态引入）
from random import randint

# 引入我们自定义的一个模块
#import test_module

# 引入模块 并取别名
#import test_package.string_utils as string_utils

# 直接引入test_package包下的string_utils模块（注意：这个写法和上面的写法意思一样）
from test_package import string_utils

if __name__ == "__main__":
    # 获取一个1-10的随机数
    r = randint(1,10)
    print(f"获取一个随机数 r={r}")
    str = "maomoa"
    print(f"str是空的吗={string_utils.is_null(str)}")