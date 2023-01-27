"""
演示json数据和python字典的相互转换

json.dumps(data) 将python数据类型转换为JSON数据类型
json.loads(data) 将JSON数据类型转换为python数据
Python语言使用JSON有很大优势，因为JSON无非是一个单独的字典或一个内部元素都是字典的列表
"""
import json  # json有特定格式的字符串

# 准备列表，列表内的每一个元素都是字典，将其转化为Json
data = [{"name":"张大山", "age":11}, {"name":"王大锤", "age":13}, {"name":"赵小黑", "age":16}]
json_str = json.dumps(data,ensure_ascii=False)  # ensure_ascii 可以写可以不写，不写默认为True 使用asc码来表示内容
print(type(json_str))
print(json_str)

# 将JSON字符串转化为Python的数据类型
s = '[{"name": "张大山", "age": 11}, {"name": "王大锤", "age": 13}, {"name": "赵小黑", "age": 16}]'
l = json.loads(s)
print(type(l))
print(l)
