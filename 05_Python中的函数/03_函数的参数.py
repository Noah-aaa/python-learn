def add(x,y):
    result = x+y
    return result

result = add(7,9)
print(f"7+9={result}")

def add(x,y):
    int_a = int(input("请输入一个整数："))
    int_b = int(input("请输入另一个整数："))
    if(x==int_a):
        print(f"原数{x}和输入参数{int_a}相等！")
    else:
        print(f"原数{x}和输入参数{int_a}不相等！")

add(5,3)