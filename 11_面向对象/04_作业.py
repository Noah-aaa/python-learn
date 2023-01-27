# 建立学生类
class Student:
    name = None
    age = None
    address = None

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


if __name__ == '__main__':
    list = []
    for i in range(1,11):
        print(f"当前录入第{i}位学生姓名，总共需录入10位学生信息。")
        name = input("请输入学生的姓名：\n")
        age = int(input("请输入学生的年龄：\n"))
        address = input("请输入学生的地址：\n")
        stu = Student(name, age, address)
        list.append(stu)
        print(f"学生{i}信息录入完成，信息为：【学生姓名：{list[i-1].name},年龄：{list[i-1].age},地址：{list[i-1].address}】")
    f = open("D:/Pycharm/python-learn/11_面向对象/stu_messages.txt", "a", encoding="UTF-8")
    f.write("学生信息：\n")
    for i in list:
        f.write(i.name+'\t')
        f.write(str(i.age)+'\t')
        f.write(i.address)
        f.write("\n")
    f.close()
    f = open("D:/Pycharm/python-learn/11_面向对象/stu_messages.txt", "r", encoding="UTF-8")
    messages = f.read()
    print(messages)
    f.close()


