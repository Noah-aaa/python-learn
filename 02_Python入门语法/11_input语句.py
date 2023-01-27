# input()接受的都是字符串
# 如果需要数字需要将输入的进行类型转换

name = input("你是谁？\n")
print("我知道了你是谁：%s"% name)
print(f"我知道了你是谁：{name}")