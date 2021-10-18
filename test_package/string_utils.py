# 如果调用者使用 * 的方式导入模块，is_null 函数将不能使用
__all__=["is_null"]

def is_null(str):
    if not str or len(str) == 0:
        return True
    return False