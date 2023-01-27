# def test():
#     num = 100
#     print(num)
# print(num)
# # 局部变量和全局变量
#global 关键字可以将函数内定义的变量声明为全局变量

num = 100
def test():
    print(num)

def test():
    num = 500
    print(num)

test()
print(num)

def test_a():
    global num
    num = 500

test_a()
print(num)