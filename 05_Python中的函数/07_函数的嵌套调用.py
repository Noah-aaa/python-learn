"""
函数的嵌套调用
"""
def func_a():
    """
    定义函数输出---1---
    :return:
    """
    print("---2---")

def func_b():
    """
    定义函数输出---1---
    ---2---
    ---3---
    :return:
    """
    print("---1---")
    func_a()
    print("---3---")

func_b()