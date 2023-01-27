# # 基本捕获语法
# # 语法：try:
# #      except:
# try:
#     f = open("D:/abc.txt",'r',encoding="UTF-8")
# except:
#     print("出现异常了，因为文件不存在，我将open的模式，改为w模式")
#     f = open("D:/abc.txt",'w',encoding="UTF-8")
# # 捕获指定异常语句
# try:
#     print(name)
# except NameError as e:
#     print("出现了变量未定义的异常")
#
# # 捕获多个异常
# try:
#     1/0
# except (NameError,ZeroDivisionError) as e:
#     print("出现了变量未定义或者除以0的异常")

# 捕获所有异常
try:
    print(name)
except Exception :  # 有异常就执行
    print("Error")
# else:  # 没有异常就执行
#     print("没有异常")
# finally:  # 无论有没有出现异常都会被执行
#     print("执行完成")