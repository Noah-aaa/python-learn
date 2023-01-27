# 字符串相关
def str_reverse(s):
    """
    将字符串反转
    :param s: 被反转的字符串
    :return: 返回已反转的字符串
    """
    return s[::-1] # 字符串也是序列
def substr(s,x,y):
    """
    完成按照给定的下标完成给定字符串的的切片
    :param s:
    :param x:
    :param y:
    :return:
    """
    return s[x:y]

if __name__ == "__main__":

    print(substr("123",0,1))
    print(str_reverse("123"))