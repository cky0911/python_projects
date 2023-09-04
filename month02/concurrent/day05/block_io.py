"""
    block_io.py
    socket 非阻塞IO示例
"""

from socket import *
from time import *

# 日志文件
f = open('log.txt', 'a+')

# tcp　服务端
sockfd = socket()
sockfd.bind(('0.0.0.0', 8888))
sockfd.listen(5)

# 非阻塞设置
sockfd.setblocking(False)

# 超时时间
# sockfd.settimeout(2)

while True:
    print("Waiting from connect...")
    # 没有客户端连接每隔3秒写一条日志
    try:
        connfd, addr = sockfd.accept()
    except (BlockingIOError, timeout) as e:
        sleep(3)
        f.write("%s : %s\n" % (ctime(), e))
        f.flush()
    else:
        print("Connect from", addr)
        data = connfd.recv(1024).decode()
        print(data)
