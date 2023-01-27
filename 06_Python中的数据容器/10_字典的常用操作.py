
my_dict = {"李易峰": 11,"林俊杰": 22,"张杰": 44}
# 字典的新增
my_dict["张信哲"] = 66
print(my_dict)

# 字典的更新
my_dict["李易峰"] =33
print(my_dict)

# 字典的删除

name = my_dict.pop("李易峰")
print(my_dict,name)

# 清空元素
my_dict.clear()
print(my_dict)

# 获取全部的key 语法：字典.keys()
my_dict = {"李易峰": 11,"林俊杰": 22,"张杰": 44}
keys = my_dict.keys()
print(keys)

# 遍历字典
# 方式一通过获取全部的key进行遍历
for key in keys:
    print(my_dict[key])
# 方式二直接通过for对字典进行遍历
for key in my_dict:
    print(my_dict[key])


# 统计字典的元素数量
print(len(my_dict))


# 字典案例练习
my_dict1 = {"王力宏":{"部门":"科技部","工资":3000,"级别": 1},
            "周杰伦":{"部门":"市场部","工资":5000,"级别": 2},
            "林俊杰":{"部门":"市场部","工资":7000,"级别": 3},
            "张学友":{"部门":"科技部","工资":4000,"级别": 1},
            "刘德华":{"部门":"市场部","工资":6000,"级别": 2}
            }
for key in my_dict1:
    if my_dict1[key]["级别"] == 1:
        my_dict1[key]["工资"] += 1000
        my_dict1[key]["级别"] += 1

print(my_dict1)

