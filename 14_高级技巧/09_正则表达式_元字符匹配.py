"""
演示python钟正则表达式使用元字符进行匹配
字符        功能
.  匹配任意一个字符除了(\n),\.匹配点本身
[] 匹配[]中列举的字符
\d  匹配数字，即0~9
\D  匹配非数字
\s  匹配空白，即空格，tab键
\S  匹配非空白
\w 匹配单词字符，即a-z,A-Z,0-9,_
\W 匹配非单词字符

也可以在[]内写规则
[a-zA-Z]
"""

import re
#
# s = "itheima1 @@python2  !!666 ##itcast3"
#
# result = re.findall(r'[a-zA-Z]',s)  ## 字符串前面带上r 表示转义字符无效，也就是普通字符的意思
# # '\d'是找出s中的所有数字，列表返回
# result = re.findall('.' , s)
# print(result)

# 匹配账号。只能由字母和数字组成，长度限制6到10位
r = '^[0-9a-zA-Z]{6,10}$'
s = '1234567893'
print(re.findall(r,s))

# 匹配QQ号,第一位不为0
r = '^[1-9][0-9]{4,10}$'

s = '_1234565'
print(re.findall(r,s))

# 匹配邮箱地址，只允许qq,163,gmail这三种邮箱
r = r'(^[\w-]+(\.[\w-]+)*@(qq|163|gmail)(\.[\w-]+)+$)'
s = 'pmo@qq.com'
print(re.match(r,s).group())
