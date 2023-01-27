name = '黑马程序员'
age = 100
price = 100.11
message = "学IT来%s,%d,%f" % (name, age, price)
print(message)

print("学it来%s\%d\%f" % (name, age, price))
# 精度设置（m.n）宽度为m,小数部分为n四舍五入

age = 11.345
print("%7.2f"%age) 

name2 = "张学良"

print(f"我是{name2}")

# 对表达式的格式化

