import socket

socket_client = socket.socket()
socket_client.connect(("localhost", 8888))
# 发送信息
while True:
    socket_client.send("你好".encode("UTF-8"))  # encode("UTF-8") 将utf-8的字符转换成字节
    # 接受返回信息

    recv_data = socket_client.recv(1024)  # 1024是缓冲区的大小，同样的recv方法是阻塞的
    print(f"服务端回复的消息是：{recv_data.decode('UTF-8')}")

# 关闭链接
socket_client.close()