def check(num):
    print("欢迎来到黑马程序员！请出示您的健康码以及72小时核酸证明，并配合测量体温！")
    if num <= 37.5:
        print("您的体温正常，欢迎光临！")
    else :
        print("您的体温异常，禁止入内！")

check(37.9)