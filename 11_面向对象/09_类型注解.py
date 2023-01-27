import json
import random
# 基础数据类型注解
var1: int = 10
var2: float = 11.2
var3: bool = True


# 类对象注解
class Student:
    pass


stu: Student = Student()


# 基础容器注解
mylist: list = [1, 2, 3]
mytuple: tuple = (1, 2, 3)
myset: set = {1, 2, 3, 3}
mydict: dict = {"itheima": 66,"itcast": 99}

# 容器类型详细注解
mylist: list[int] = [1, 2, 3]
mytuple: tuple[int, int, int] = (1, 2, 3)
myset: set[int] = {1, 2, 3, 3}
mydict: dict[str, int] = {"itheima": 66, "itcast": 99}

# 在注释中进行类型注释
var_1 = random.randint(1, 10)  # type: int
var_2 = json.loads('{"name": "zhangsan"}')  # type:dict[str,str]


def func():
    return 10


var_3 = func()  # type:int

# 一般能直接看出来或者有直接定义的变量就不需要使用注解。一般无法直接看出来变量类型时会添加变量的类型注解
# 类型注解不会影响程序的运行，注解只是提示性的。


