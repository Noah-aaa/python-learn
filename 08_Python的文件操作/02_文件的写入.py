"""
演示文件的写入 文件存在会清空原有内容写入新内容
文件不存在会新增文件，并将内容写入
"""
import time
# 打开文件，不存在的文件
f = open("D:/test.txt", "w", encoding="UTF-8")

# write写入
f.write("hello world") # 将内容写入内存中
# time.sleep(5)  # 休眠5秒钟
# f.flush()   # 将内容写入硬盘中

# 关闭文件
f.close() # 内置flush方法

# 打开已经存在的文件
f = open("D:/test.txt", "w", encoding="UTF-8")
f.write("黑马程序员")
f.flush()
f = open("D:/test.txt", 'r', encoding="UTF-8")
print(f.read())
f.close()
# f.close()