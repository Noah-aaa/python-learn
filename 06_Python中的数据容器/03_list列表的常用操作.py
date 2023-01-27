mylist = ["itcast","itheima","Python"]

#1.1查找某元素在列表内的下表索引  语法 列表.index("被查找元素")
itheima = mylist[1]
index = mylist.index(itheima)
index = mylist.index("itheima")
print(index)
#1.2 查找元素不存在，会报错
# index = mylist.index("hello")
# print(index)

#2. 修改特定下标索引值     语法  列表[下标索引] = "修改的值"
mylist[0] = "龙腾"
print(f"修改后的列表值为：{mylist}")

#3.在指定下标位置插入新元素   语法 ( 列表.insert(指定下标,"插入元素"))
mylist.insert(1, "best")
print(f"列表插入后的值为：{mylist}")

#4.在列表的尾部追加单个新元素   语法(列表.append("元素") )
mylist.append("黑马程序员")
print(f"追加单个新元素后的列表为：{mylist}")

#5. 在列表的尾部追加一批元素  语法 列表.extend("列表")
list = [[1,2,3],[4],[5,6,7,8]]
mylist.extend(list)
print(f"追加列表list后的值为：{mylist}")

#6. 删除指定下标元素
mylist = ["itcast","itheima","python"]
# 语法一：del列表[下标] 语法二：列表.pop(指定下标)。
# 区别：语法一只是删除指定的下标元素。语法二删除指定下标元素并且返回删除元素

#6.1通过语法一删除元素

del mylist[2]
print(f"通过语法一删除元素后，列表的值为{mylist}")

#6.2通过语法二删除元素并返回删除后元素
mylist = ["itcast","itheima","python"]
element = mylist.pop(2)
print(f"通过语法二删除元素后的列表值为{mylist}和删除元素的{element}")

#7.删除某元素在列表中的第一匹配项
mylist = ["itcast","itcast","itheima","itheima","Python"]
mylist.remove("itcast")
print(f"删除某元素在列表中的第一个匹配项之后的列表为{mylist}")

#8.清空列表
mylist.clear()
print(f"清空之后的列表{mylist}")

#9.统计列表内某元素的数量
mylist = ["itheima","itcast","itheima","itheima","itheima","Python"]
count = mylist.count("itheima")
print(f"列表中itheima的数量是{count}")
#10.统计列表中的元素数量多少
count =len(mylist)
print(f"列表中的元素个数有{count}个")


# 练习案例

list = [21,23,21,23,22,20]
list.append(31)
new_list = [29,33,30]
list.extend(new_list)
print(list[0])
j= None
for i in range(len(list)):
    j=i
print(list[i])
print(list.index(31))