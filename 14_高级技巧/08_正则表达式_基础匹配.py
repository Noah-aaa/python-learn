import re

s = "python itheima pythonpython"

result = re.match("python", s)  # match()方法是从头开始匹配的，如果头没有它就不会进行下去。
print(result.span())  # 返回下标区间
print(result.group())  # 返回匹配的字符串

# 如果从头开始没有的话，那么后面result返回的都是None

# search()方法搜索整个字符串，返回第一个搜索的下标和结果
# 不存在返回None

result = re.search('python', s)
print(result.group())
print(result.span())


# 更高级的方法
# findall() 找到整个匹配的所符合的字符串 返回列表list[],如果没有的话那么返回的就是空列表


result = re.findall('python', s)
print(result)