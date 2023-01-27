my_str = "itheima and itcast"

"""
字符串不能更改
"""

# 字符串index寻找下标

index = my_str.index("and")
print(index)

# 字符串替换replace函数

new_str = my_str.replace("it" , "程序")
print(new_str)
print(my_str)

# 字符串的分割 语法：字符串.split(分隔符字符串)

mystr = "itcast itheima hello python"
mystr_list = mystr.split(" ")
print(f"mystr_list的类型是{type(mystr_list)},内容是{mystr_list}")

# strip方法 语法：字符串.strip(参数)  不写参数默认参数是空格，也可以自定义参数。默认去除前后空格，也可以自定义参数去除

mystr = "  itcast itheima hello python  "
mystr_list = mystr.strip()
print(f"{mystr}被strip方法之后的结果是{mystr_list},类型为{type(mystr_list)}")

mystr = "12itcast itheima hello python21"
mystr_list = mystr.strip("12")
print(f"{mystr}被strip方法之后的结果是{mystr_list},类型为{type(mystr_list)}") #参数 "12" ,并不是完全按照参数删除字符串，只要满足其中之一是子串就可以满足。


# 统计字符串中某字符串出现的次数，count字符串需要参数
mystr = "12itcast itheima hello python21"
#count = mystr.count("it")
# print(f"{mystr}中的it出现了{count}次")

# count = mystr.count()
# print(count) 错误语法


# 统计字符串长度 len()函数
mystr = "12itcast itheima hello python21"
len = len(mystr)
print(f"字符串{mystr}的长度为{len}")

# 字符串练习案例

str = "itheima itcast boxuegu"

#统计字符串内有多少个it字符

count = str.count("it")

# 将字符串中的空格全部换成字符"|"

str = str.replace(" ","|")

# 并按照“|”进行分割，得到列表

str_new = str.split("|")

print(f"{count},{str}，{str_new}")



