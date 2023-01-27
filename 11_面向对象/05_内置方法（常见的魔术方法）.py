# 定义一个Student类
class Student:
    name = None
    age = None

    def __init__(self, name, age):  # 构造方法
        self.name = name
        self.age = age

    def __str__(self):  # 内置转字符串方法 将类队象内容转换为字符串
        return f"{self.name}, {self.age}"

    def __lt__(self, other):  # 通过比较对象的大小返回True或者False,指定比较对象的成员变量 只能用于小于和大于上判断
        return self.name < other.name

    def __le__(self, other):  # 只可以可以用于<=,>=的判断
        return self.age <= other.age

    def __eq__(self, other):
        return self.age == other.age


# 构造方法直接输出对象，只会得到内存地址
stu1 = Student("周杰伦", 29)
print(stu1)  # 得到内存地址
print(str(stu1))  # 得到内存地址


# __str__魔术方法
stu = Student("周杰伦", 29)
print(stu)  # 得到对象内容的字符串


# __lt__  比较小于方法
stu2 = Student("周杰伦", 29)
print(stu1 <= stu2)
print(stu1 >= stu2)


# __eq__ 对象中判断是否相等 不用此方法进行比较 == 那么比较的是内存地址，
# 那么虽然不报错但是还是会有问题，一直都是false因为不是同一个变量，所以内存地址肯定不同

print(stu1 == stu2)
print(stu1.name == stu2.name)
