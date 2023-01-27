# age = int(input("请输入年龄："))
# sex=str(input("请输入性比："))
# if int(input("请输入年龄："))>= 18:
#     if (str(input("请输入性比："))=='男') :
#         print("恭喜你符合条件")
#     else:
#         print("你不符合条件")
# else :
#     print("你的输入有问题，请重新输入")

age = 20
year = 3
level = 1
if age>= 18:
    print("你是成年人")
    if age< 30:
        print("你的年龄达标了")
        if year > 2:
            print("恭喜你，年龄和入职时间都达标了，可以领取礼物了")
        elif level > 3:
            print("恭喜你，所有都达标了，可以领取礼物了")
        else :
            print("不好意思，入职时间和级别不达标。")
    else:
        print("不好意思。年龄太大了")
else :
    print("这是成年人专享礼物，未成年人不可以领取")