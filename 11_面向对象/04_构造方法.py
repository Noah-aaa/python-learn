# 构造方法的语法__init__

class Student:
    name = None
    age = None
    tel = None

    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel


stu_1 = Student("周杰伦", 18, '1222222222')
print(f"学生1的名字是{stu_1.name},年龄是{stu_1.age},电话号码是{stu_1.tel}")
