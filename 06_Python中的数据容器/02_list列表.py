"""
演示数据容器之：list列表
语法 [元素，元素，元素........]
嵌套语法[[元素，元素......],[元素,元素.......]]
元素类型无限制，可以为任何类型。
优雅高级的语言
下标索引可以从前后方向进行
从前往后的方向，编号从0开始递增
从后往前的方向，编号从-1开始递减
"""
name_list = ['itheima','itcast','python']
print(name_list)

print(type(name_list))

my_list = ["itheima",6666,True]

print(my_list)
print(type(my_list))


mytest_list = [[1,'是',1],[2,"不是",3]]
print(mytest_list)
print(type(mytest_list))

for i in range(0,3): # range函数是从 start开始数到stop结束数，但是不包括stop结束数 0，1，2
    print (name_list[i])

for i in range(2):
    for j in range(3):
        print(mytest_list[i][j], end='\t')
print('\n')
print(mytest_list[-1])
print(mytest_list[-2])
# print(mytest_list[-3])