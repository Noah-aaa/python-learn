"""
类的定义和使用
class 类名:
    类的属性
    类的行为（即定义类的函数）
创建对象名 对象名字 = 类名（）

在类里面的成员方法需要使用self关键字，通过self.变量名调用类里面的参数进行输出
def test:
    name = None
    age = None
    def getName(self):
        return self.name

test_1 = test() 构造对想

"""


class Student:
    name = None  # 学生的名字

    def say_hi(self):
        print(f"{self.name}说大家好！")  # 成员方法

    def say_hi2(self, msg):
        print(f"大家好，我是{self.name},{msg}")  # 访问成员属性必须要加self关键字，如果是访问外部变量不需要访问成员变量


stu_1 = Student()
stu_1.name = "刘亦菲"
stu_1.say_hi()

stu_2 = Student()
stu_2.name = "刘德华"
stu_2.say_hi2("我很高兴见到大家，在这里祝大家新年快乐，在新的一年有新的气象！")