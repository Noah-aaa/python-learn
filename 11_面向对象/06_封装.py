class Phone:
    __current_voltage = 1  # 私有成员方法和成员变量需要使用两个下划线进行设置 __

    def __keep_single_core(self):
        print("让cpu单核运行！")

    def call_by_5g(self):
        if self.__current_voltage >= 1:
            print("5g通话已经开启")
        else:
            self.__keep_single_core()


phone = Phone()
# phone.__current_voltage = "www"  # 可以重新赋值，并且输出
# print(phone.__current_voltage)  # 但是如果直接调用不可以的
phone.call_by_5g()