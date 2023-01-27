def list_while_func():
    """

    :return:
    """
    mylist = ["传智教育","黑马程序员","Python"]
    index = 0
    while index<len(mylist):
        print(f"列表中第{index+1}个数为{mylist[index]}")
        index +=1

list_while_func()

def list_for_func():
    mylist = ["传智教育","黑马程序员","Python"]
    # index = 0
    for index in range(len(mylist)):
        print(f"列表中第{index+1}个值为{mylist[index]}")
    for i in mylist:
        print(f"列表中的元素有{i}")

list_for_func()


# 练习案例
list =[1,2,3,4,5,6,7,8,9,10]

def list_select_func(list):
    newList = []
    for element in list:
        if element%2==0:
            newList.append(element)
    return newList

newList = list_select_func(list)
print(f"新列表为{newList}")
