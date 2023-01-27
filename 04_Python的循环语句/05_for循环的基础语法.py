name = "itheima"
for x in name :
    print(x)


# 练习案例，数一数有几个字母a
# 判断有几个字母。

name = "itheima is a brand of itcast"
count = 0
for x in name:
    if x == 'a':
        count += 1
print(f"{name}中共含有{count}个字母a")
print("%s中共含有%d个字母a"% (name , count))