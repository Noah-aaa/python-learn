# 简单的闭包

# def outer(logo):
#
#     def inner(msg):
#         print(f"<{logo}>{msg}<{logo}>")
#
#     return inner
# # 闭包操作，类似于函数定义函数
#
# fn1 = outer("heimai")  # 对于outer来说fn1是临时的存储的，但是对于inner来说这是一个不变的变量
# fn1("黑马")
# fn1("吊毛")
#
# fn2 = outer("baobei")
# fn2("nihao")
# fn2("heui")

# 使用nonlocal关键字修改外部函数的值
#
# def outer(num1):
#
#     def inner(num2):
#         nonlocal num1  # 没有nonlocal关键字就没办法修改num1的值
#         num1 += num2
#         return num1
#
#     return inner
#
# fn = outer(100)
# print(fn(10))


# 使用闭包实现ATM小案例

def account_create(initial_amount):

    def atm(num, deposit=True):
        nonlocal initial_amount
        if deposit:
            initial_amount += num
            print(f"存款，+{num}, 账户余额：{initial_amount}")
        else:
            initial_amount -=num
            print(f"取款，-{num}, 账户余额：{initial_amount}")

    return atm   # 内部函数，atm

fn = account_create(10000)
fn(122, False)

"""
闭包优点：
1.无须定义全局变量即可实现通过函数，持续的访问、修改某个值
2.闭包使用的变量所用于函数内，难以被错误的调用修改

缺点：
由于内部函数持续引用外部函数的值，所以会导致一部分内存空间不会被释放，一直占用内存


什么是闭包
定义双层函数，内层函数可以访问外层函数的变量
将内层函数作为外层函数值返回，此内层函数就是闭包函数



nonlocal 关键字
在闭包函数（内部函数中）想要修改外部函数的变量值
需要用nonlocal声明这个外部变量
"""
