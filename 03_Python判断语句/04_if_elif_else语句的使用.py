height = int(input("请输入你的身高（cm）："))
vip_level = int(input("请输入你的vip等级（1-5）："))
day = int(input("请告诉我今天是几号："))
if height < 120:
    print("身高小于120cm,可以免费游玩")
    if day==1:
        print("今天可以打九折")
    else :
        print("不好意思，今天没有折扣")
elif vip_level >3:
    print("VIP等级大于3，可以免费游玩")
else :
    print("不好意思，条件都不满足，需要购票要10")
