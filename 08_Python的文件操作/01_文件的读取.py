
"""
必须要使用关键字传参，因为encoding不是位置指定
"""
import time

# 打开文件
f = open("D:\新建文件夹\Test.txt", "r", encoding="utf-8")
print(type(f))
# 读取文件 - read() 括号里面带数字就是读多少字符会把换行读进去，不带参数就是读全部的内容,
# 同时读出来的结果是str字符串

print(f"读取10个字符的结果是{f.read(10)}")
print(f"读取全部内容的结果是{type(f.read())}")

# 读取文件 - readlines() # 读取全部行包括换行符号，且读出来的类型是列表list[]
f = open("D:\新建文件夹\Test.txt", "r", encoding="utf-8")
lines = f.readlines()
print(f"读取全部内容的结果是{lines},类型是{type(lines)}")

# 读取文件 - readline() # 读取一行数据
f = open("D:\新建文件夹\Test.txt", "r", encoding="utf-8")
line1 = f.readline()
line2 = f.readline()
line3 = f.readline()

print(line1.strip())
print(line2.strip())
print(line3.strip()) # strip()函数默认是去除字符串的前后空格
f.close()

# for循环读取文件行 ## 读取每一行数据
f = open("D:\新建文件夹\Test.txt", "r", encoding="utf-8")
for line in f:
    print(line)

# 关闭文件，如果不关闭。python会一直占用文件，导致无法对文件进行操作

f.close()
time.sleep(5) # 以秒为单位50000秒Python
# sleep ()函数用法：线程睡眠 位于 time 模块中的 sleep (secs) 函数，
# 可以实现令当前执行的线程暂停 secs 秒后再继续执行。 所谓暂停，即令当前线程进入阻塞状态，
# 当达到 sleep () 函数规定的时间后，再由阻塞状态转为就绪状态，
# 等待 CPU 调度

# with open()语法操作文件
with open("D:\新建文件夹\Test.txt","r",encoding="UTF-8") as f: # 自动关闭文件
    print(f.read().count("黑马"))

