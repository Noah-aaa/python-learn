for x in range(10):
    print(x,end=' ')
print()
for x in range(5,10):
    print(x,end=' ')
print()
for x in range(5,10,2):
    print(x,end=' ')
print()
num = int(input("请输入一个数字（从1开始到这个数）中有几个偶数："))
count = 0
for x in range(1,num):
    if x%2 == 0:
        count+=1
print(f"从1到{num}中有{count}个偶数")