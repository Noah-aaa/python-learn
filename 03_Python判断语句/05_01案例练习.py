import random
num = random.randint(1,10)
while True:
    getNum = int(input("请输入你猜的数字"))
    if getNum == num:
        print("恭喜你，猜对了。")
        break;
    elif getNum > num:
        print("猜大了")
    else:
        print("猜小了")
