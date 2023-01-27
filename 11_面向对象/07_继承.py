# 演示单继承
class Phone:
    IMEI = None
    producer = "HM"


    def call_by_4g(self):
        print("4g通话")


class Phone2022(Phone):
    face_id = "111111"

    def call_by_5g(self):
        print("5g通话")


phone = Phone2022()
print(phone.IMEI)

# 演示多继承

class NFCReader:
    nfc_type = "第五代"
    producer = "HM"

    def read_card(self):
        print("NFC读卡")

    def write_card(self):
        print("NFC写卡")


class RemoteControl:
    rc_type = "红外遥控"

    def control(self):
        print("红外遥控开启了！")


# 定义子类
class Myphone(Phone2022, NFCReader, RemoteControl):  # 如果在继承父类中存在同名属性的话，先来的先执行，前面会覆盖前面
    pass  # pass关键字可以在类里面不写语句 可以保证类的定义完整性



myphone = Myphone()
myphone.call_by_4g()


