"""测试一个经典的GUi程序的写法，使用面向对象的方式"""

from tkinter import *
class Application(Frame):
    """一个经典的gui程序的类的写法"""
    def _init_(self,master = None):
       super()._init_(master) # super()代表的是父类的定义，而不是父类的对象
       self.master = master
       self.pack()
       self.createWidget()


    def createWidget(self):
        pass


root = Tk()
root.geometry("400x200+200+300")
root.title("一个经典的GUI程序")

app = Application(master = root)
root.mainloop()