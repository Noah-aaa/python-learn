"""
演示数据容器集合的使用

# 集合 不重复且无序，<不支持下标索>引进行访问(集合不是序列)
可以进行修改
"""
# 定义集合
myset = {"传智教育","黑马程序员","itheima","itcast","python""传智教育","黑马程序员","itheima","itcast","python"}
mysetempty = set()

print(f"myset的内容是{myset},类型是{type(myset)}")
print(f"mysetempty的内容是{mysetempty},类型是{type(mysetempty)}")

# 添加新元素
myset.add("Pycharm")
print(myset)

# 移除元素 集合.remove(元素)

myset.remove("黑马程序员")
print(myset)

# 集合.pop() 随机去除一个元素
myset = {"传智教育","黑马程序员","itheima","itcast","python","传智教育","黑马程序员","itheima","itcast","python"}
element= myset.pop()
print(f"随机取出的元素是：{element},取出之后还剩下{myset}")

# 清空集合
myset.clear()
print(myset)

# 取两个集合的差集 两个集合原本不变，得到一个新的集合，新的集合set3中就是set1中在set2中没有的元素，
set1 = {1,2,3}
set2 = {1,5,6}
set3 = set1.difference(set2)
print(set3)

# 消除两个集合的差集 语法：集合1.difference_update(集合2)
# 功能对比集合1和集合2，在集合1内，删除和集合2相同的元素
# 结果集合1被修改，集合2没有改变
set1 = {1,2,3}
set2 = {1,5,6}
set1.difference_update(set2)
print(set1 , set2)

# 2个集合合并成一个集合 union()
set3 = set1.union(set2)
print(f"合并后集合为{set3}")  # 集合会去重

# 统计元素数量
lenth = len(set2)
print(lenth)

# 集合的遍历 集合不支持while循环，因为它不能通过下标访问。但是它可以通过for循环访问

for element in set3:
    print(f"set3集合中有元素：{element}")



# 集合案例练习
my_list = ['黑马程序员','传智播客','黑马程序员', 'itheima','itcast','itheima','itcast','best']
my_set = set()
for element in my_list:
    my_set.add(element)
print(f"最终的集合是：{my_set}")