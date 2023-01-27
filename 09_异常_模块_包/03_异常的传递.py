def func1():
    print("func1开始执行")
    num = 1/0
    print("func2结束执行")

def func2():
    print("func2开始执行")
    func1()
    print("func2结束执行")

def main():
    try:
        func2()
    except Exception as e:
        print(f"出现的异常内容是：{e}")
    else:
        print("运行没有问题")
    finally:
        print("已经执行过了")
main()