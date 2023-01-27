"""
装饰器的写法
"""
# 一般的装饰器的一般写法（闭包）

# def outer(func):
#     def inner(name):
#         print(f"{name}要睡觉了")
#         func(name)
#         print(f"{name}要起床了")
#     return inner
#
#
# def sleep(name):
#     import random
#     import time
#     print(f"{name}正在睡觉中")
#     time.sleep(random.randint(1, 5))
#
#
# fn = outer(sleep)
# fn("longteng")

# import random

# import random
# print(random.randint(1, 5)) # 只能取到1到5之间也就是取不到5


# 装饰器的快捷写法（语法糖）
def outer(func):
    def inner(name):
        print(f"{name}要睡觉了")
        func(name)
        print(f"{name}要起床了")
    return inner


@outer   # 语法
def sleep(name):
    import random
    import time
    print(f"{name}正在睡觉中")
    time.sleep(random.randint(1, 5))


sleep("longteng")
"""
什么是装饰器
装饰器就是使用创建一个闭包函数，在闭包函数内调用目标函数，
可以达到不改动目标函数的前提下，增加额外的功能。
"""