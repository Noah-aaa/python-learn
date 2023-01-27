# 列表
my_list = [["a", 33],["b", 55],["c", 11]]

# 排序基于带名函数
# def list_sort(list):
#     return list[1]
# my_list.sort(key=list_sort,reverse=True)
# print(my_list)

# 排序，基于lambda匿名函数
my_list.sort(key=(lambda element: element[1]), reverse=True)
print(my_list)