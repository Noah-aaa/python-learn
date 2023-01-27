"""
演示socket服务端的开发
"""
import socket

# 创建Socket对象
socket_server = socket.socket()
# 绑定ip地址和端口
socket_server.bind(("localhost", 8888))
# 监听端口
socket_server.listen(1)  # listen方法内接受一个整数传参，表示接受的链接数量

# result: tuple = socket_server.accept()  # 接受的是二元元组
# conn = result[0]  # 客户端和服务端的链接对象
# address = result[1]  # 客户端的地址信息
conn, address = socket_server.accept()  # 等于上三行注释代码，可以像这样直接等于这种格式
# accept方法是阻塞的方法，等待客户端的链接。如果没有链接，就卡在这一行不想下执行了。
print(f"接收到了客户的信息，客户端的信息是{address}")
while True:
    # 接受客户端信息, 要是使用客户端和服务端的本次链接对象，而非socket_server对象
    data: str = conn.recv(1024).decode("UTF-8")  # recv接受的参数是缓冲区的大小，一般给1024即可
    # recv方法的返回值是一个字节数组也就是bytes对象，不是字符串，可以通过decode方法通过UTF-8编码，将字节数转换为字符串对象
    print(f"客户端发来的消息是：{data}")
    # 发送回复信息
    msg = input("请输入你要和客户端回复的消息：")
    if msg == 'exit':
        break
    conn.send(msg.encode("UTF-8")) # 解码
# 关闭链接
conn.close()
socket_server.close()