"""
演示数据容器的通用操作
"""
my_list = [1,2,3,4,5]
my_str = "abcdefg"
my_tuple = (1,2,3,4,5)
my_dict = {"key1": 1,"key2": 2,"key3": 3,"key4": 4, "key5": 5}
my_set = {1,2,3,4,5}

# 通用操作之一 len()
print(len(my_list))
print(len(my_str))
print(len(my_tuple))
print(len(my_dict))
print(len(my_set))

# 通用操作 max() 求最大值
print(max(my_list))
print(max(my_str))
print(max(my_tuple))
print(max(my_dict))
print(max(my_set))

# 通用操作 min() 求最小
print(min(my_list))
print(min(my_str))
print(min(my_tuple))
print(min(my_dict))
print(min(my_set))

# 通用类型转换 list(),tuple(),set(),str()
print(f"列表转列表的结果是：{tuple(my_list)}")
print(f"元组转列表的结果是：{tuple(my_tuple)}")
print(f"字符串转列表的结果是：{tuple(my_str)}")
print(f"集合转列表的结果是：{tuple(my_set)}")
print(f"字典转列表的结果是：{tuple(my_dict)}")
# 数据容器无法转字典，除了字典本身。

# 排序功能sorted() ,从小到大输出 排序结果会变成列表队象。
print(sorted(my_list))
print(sorted(my_tuple))
print(sorted(my_set))
print(sorted(my_dict))
print(sorted(my_str))

# 反向排序
print(sorted(my_list,reverse = True))