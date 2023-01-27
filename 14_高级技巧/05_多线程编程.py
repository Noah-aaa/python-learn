import time
import threading

def sing(msg):
    while True:
        print(msg)
        time.sleep(1)


def dance(msg):
    while True:
        print(msg)
        time.sleep(1)

if __name__ == '__main__':
    sing_thread = threading.Thread(target=sing, args=("我要唱歌，哈哈哈",))  # 创建一个唱歌线程
    dance_thread = threading.Thread(target=dance, kwargs={"msg":"我在跳舞啦啦啦"})  # 创建一个跳舞的线程

    sing_thread.start()
    dance_thread.start()


"""

多线程语法：
导包
import threading
构建进程对象
thread_obj = threading.Thread([group[,target[,name[,args[,kwargs]]]]])

调用进程
thread_obj.start()


grop :暂时无用
target :执行的目标任务名
args: 以元组的方式个执行任务传参
kwargs : 以字典的方式给执行任务传参
name : 线程名，一般不用设置
"""