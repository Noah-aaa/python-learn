import random
money = 10000
for num in range(1,21):
    score = random.randint(1, 10)
    if score < 5:
        print(f"员工{num},绩效分{score},低于5，不发工资，下一位。")
        continue
    else:
        if money <= 0:
            print("工资发完了，下个月领取吧")
            break
        else:
            money -= 1000
            print(f"员工P{num}发放工资1000元，账号余额还剩{money}元")