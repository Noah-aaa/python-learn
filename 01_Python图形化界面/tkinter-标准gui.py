from tkinter import *
from tkinter import messagebox


root = Tk()    # 创建窗口对象

root.title("这是我第一个gui程序")
root.geometry("500x300")     # 500长x300宽 +100是据左边屏幕的100的位置，+200是据上边屏幕的200的位置，如果是-100那么就是距离右边屏幕100的位置，同理下面屏幕也是一样的。

btn01 = Button(root)
btn01["text"] = "点我就送花"
btn01.pack()
def getFlower(e):
    # e事件对象
    messagebox.showinfo("message","送你一朵玫瑰花，亲亲我吧！")
    print("送你99朵玫瑰！")

btn01.bind("<Button-1>",getFlower)

root.mainloop() # 调用mainloop方法，进入事件循环