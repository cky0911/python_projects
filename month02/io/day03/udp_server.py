"""
    udp_server.py udp服务端
    重点代码
"""

from socket import *

# 创建UDP套接字
sockfd = socket(AF_INET, SOCK_DGRAM)

# 绑定地址
server_addr = ('127.0.0.1', 8888)
sockfd.bind(server_addr)

# 循环收发
while True:
    data, addr = sockfd.recvfrom(1024)
    print("receive message from client %s and content is: %s" % (addr, data.decode()))
    sockfd.sendto(b'Thanks', addr)

# 关闭套接字
sockfd.close()
