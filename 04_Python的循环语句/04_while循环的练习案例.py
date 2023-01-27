# 使用while语句打印九九乘法表
# 控制变量 i，j的值，类似于java和C语言的九九乘法表，除了语法问题，其余的思维一样的
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f"{j}*{i}={i*j}\t" , end='')
        j += 1
    i += 1
    print()
        #print("\n"d)


print("这是我想要输入的内容 并且用作为换行的条件" , end='*')
print('*')
print("这就已经换行了")

name = "itheima"

for x in name:
    print(f"itheima的字符为{x}\t")
