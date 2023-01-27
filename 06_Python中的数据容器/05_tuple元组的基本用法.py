# 定义元组
"""
元组与列表部分类似，
1.元素类型不限制
2.元组不许修改，但是列表可以修改
3.元组是用小括号，列表是用中括号
"""
t1 = (1,"hello",True)
t2 = ()
t3 = tuple()
print(f"t1的类型是：{type(t1)},t1的内容是{t1}")
print(f"t2的类型是：{type(t2)},t2的内容是{t2}")
t4 = ("hello") # 如果括号内只有单元素的话，必须要加逗号，才能保证是元组
print(f"t4的类型是：{type(t4)},t4的内容是{t4}")
t5 = ("hello",)
print(f"t5的类型是：{type(t5)},t5的内容是{t5}")
# 元组的嵌套
t5 = ((1,2,3,4,5),(6,7,8),(10,11,12,...,100))
# 利用下标索引取元组元素
num = t5[0][4]
print(num)

# 元组的操作，index查找方法 元组.index(查找元素) 返回下标
index = t5.index((1,2,3,4,5))
print(f"查找(1,2,3,4,5)这个元素的下标为：{index}")
t5 = ("I","Love","You")
index = t5.index("Love")
print(f"查找的Love的下标为{index}")

# 元组的计数，统计元组中，count方法

count = t5.count("Love")
print(f"Love在该元组出现的次数为：{count}")

# 元组len函数统计元组元素个数

num= len(t5)
print(f"元组的个数为{num}")

# 元组的遍历
"""
while and for 循环语句
"""

# while 循环
### 优雅高效的语言

index = 0
while index < len(t5) :
    print(f"元组的元素有{t5[index]}")
    index += 1

# for循环
for element in t5:
    print(f"元组的元素有{element}",end='_\"高级\"')
print("\n")
# 元组只读，不能修改

# 定义一个元组
t6 = (1,2,["itheima","itcast"])
print(t6[2][1])
t6 [2][1] ="itheima"
print(t6)

"""
元组特性：
可以容纳多个数据
可以容纳不同类型数据（混装）
数据是有序存储的
允许重复出现
不可以修改（增加或删除）
支持 for 循环
多数特性和list一致，不同点在于不可以修改
但是可以修改内部嵌套内部list列表，允许列表修改

"""

# 元组的基本操作练习案例


tuple_new = ('周杰轮',11,['football','music'])
# 定义学生姓名，年龄，爱好

index = tuple_new.index(11)
# 得到年龄下标

# 查询学生的姓名

name = tuple_new[0]

# 删除学生爱好中的 football

# del tuple_new[2][1]
tuple_new[2].pop(1)

#增加爱好：coding到爱好list内

tuple_new[2].append("coding")

print(name)
print(tuple_new)
