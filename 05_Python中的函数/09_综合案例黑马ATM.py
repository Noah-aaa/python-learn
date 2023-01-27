#定义全局变量
name = None
money = 5000000
name = input("请输入您的姓名：")
#定义查询函数
def query():
    """

    :return:
    """
    print("-----------查询余额-------------")
    print(f"{name}，你好，您的余额剩余：{money}元。")

def saving( num):
    """

    :param num:
    :return:
    """
    global money
    money += num
    print("--------存款----------")
    print(f"{name}，您好，您存款{num}元。")
    query()

def get_money(num):
    """

    :param num:
    :return:
    """
    global money
    money -= num
    print("---------取款---------")
    print(f"{name}，您好，您取款{num}元")
    query()

#主菜单界面
def main():
    """

    :return:
    """
    print("---------------主菜单-------------")
    print("查询余额\t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输出4]")
    return input("请输入您的选择：")

while True:
    keyboard_input = main()
    if int(keyboard_input)==1:
        query()
    elif int(keyboard_input)==2:
        num = int(input("请输入存款的金额："))
        saving(num)
    elif int(keyboard_input)==3:
        num = int(input("请输入取款金额："))
        get_money(num)
    elif int(keyboard_input)==4:
        break # 正常的退出程序，没问题。
    else:
        print("输入错误，请输入正确指令")
        break # 通过break退出循环，不正常退出循环。


