class Phone:
    IMEI = None
    producer = "ITCAST"

    def call_by_5g(self):
        print("正在使用5g通话")


# 定义子类，和复写父类成员

class MyPhone(Phone):
    producer = "heima"

    def call_by_5g(self):
        print("开启cpu单核模式，确保通话时更省电")
        # 方式一调用父类的成员 可以用 父类.成员变量  父类.成员方法(self)
        Phone.call_by_5g(self)
        # 方式二 通过super关键字 super().成员变量 super().成员方法()
        super().call_by_5g()

phone = MyPhone()
print(phone.call_by_5g())