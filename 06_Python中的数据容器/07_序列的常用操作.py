"""
什么是序列？
内容连续、有序、可使用下标索引的一类数据容器
列表、元组、字符串，均可以视为序列
序列的基本操作
常用操作 ，切片
从一个序列中，取出一个子序列就是切片
语法：序列[起始下标：结束下标：步长] 默认不写起始下标就是从0开始，不写结束下标就是到序列末尾，步长不写默认就是取 1
反向取，则起始下标和结束下标都要进行互换
"""
mylist = [1,2,3,4,5,6]
# 对list进行切片，从1开始，4结束，步长1
list_new = mylist[1:4:1]
print(list_new)

# 对tuple元组进行切片，从头开始，到结尾结束。步长为1
my_tuple = ("1",2,"1+2=3，我告诉你这个是错的",[1,2,3])
tuple_new = my_tuple[:]
print(tuple_new)

# 对str字符串进行切片，从头开始到结尾结束，步长2

Str = "1234567789"
str_new = Str[::2]
print(str_new)

# 对str进行切片，从头开始，到结尾结束步长为-1 # 反过来取值也就是字符串反转

str_new = Str[::-1]
print(str_new)

# 对列表进行切片，从3开始，到1结束，步长为-1

list_new = mylist[3:1:-1]
print(list_new)


# 对元组进行切片，从头开始，到结尾结束，步长为-2

tuple_new = my_tuple[::-2]
print(tuple_new)

# 序列的切片操作
myStr = "万过薪月，员序程马黑来，nohtyp学"
# new_Str = myStr[::-1]
# index = new_Str.index("黑马程序员")
# print(f"得到的字符串的是{new_Str[index:index+5:1]}")

print(f'输出的是：{myStr[myStr.index("黑"):myStr.index("员")-1:-1]}')