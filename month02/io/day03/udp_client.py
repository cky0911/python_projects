"""
    udp_client.py  udp客户端
    重点代码
"""

from socket import *

# 服务器地址
ADDR = ('127.0.0.1', 8888)

# 创建套接字
sockfd = socket(AF_INET, SOCK_DGRAM)

# 循环发送消息
while True:
    data = input("send message to server:")
    # 直接回车跳出循环 服务端不需要做什么操作  因为无连接
    if not data:
        break
    sockfd.sendto(data.encode(), ADDR)
    msg, addr = sockfd.recvfrom(1024)
    print("receive message from server:", msg.decode())

sockfd.close()

# 不像TCP需要服务端先启动
