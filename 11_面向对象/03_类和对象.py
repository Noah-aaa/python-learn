# 设置一个闹钟类
class clock:
    id = None
    price = None

    def ring(self):
        import winsound
        winsound.Beep(2000,3000)


# 构建2个闹钟对象并让其工作

clock1 = clock()
clock1.id = "001"
clock1.price = 9.99
clock1.ring()


clock2 = clock()
clock2 = clock()
clock2.prince = 99.9
clock2.ring()
