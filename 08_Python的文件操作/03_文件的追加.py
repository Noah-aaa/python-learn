
"""
a模式下 文件不存在会创建文件
文件存在会进行追加，不会清空原有的内容只在后面进行追加
"""
# 打开文件，不存在的文件
f = open("D:/test.txt", "a", encoding="UTF-8")
f.write("黑马程序员")
# 刷新
f.flush()
# 关闭
f.close()
f = open("D:/test.txt", "a", encoding="UTF-8")
f.write("学习python最佳选择")
f.close()
