"""
    fork_server.py  基于fork的多进程并发模型
    目标：连接多个客户端 为多个客户端提供服务

    1.创建监听套接字
    2.等待接收客户端请求
    3.客户端连接创建新的进程处理客户端请求
    4.原进程继续等待其他客户端连接
    5.如果客户端退出，则销毁对应的进程
"""

from socket import *
import os
import signal

ADDR = ('0.0.0.0', 8888)


# 客户端处理函数,循环收发消息
def handle(c):
    while True:
        data = c.recv(1024).decode()
        if not data:
            break
        print(data)
        c.send(b'OK')


# 创建监听套接字
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # 设置端口立即重用
s.bind(ADDR)
s.listen(5)

# 处理僵尸进程
# signal.signal(signal.SIGCHLD, signal.SIG_IGN)
print("Listen the port 8888....")

while True:
    # 循环等待客户端连接
    try:
        c, addr = s.accept()
        print("Connect from", addr)
    except KeyboardInterrupt:
        os._exit(0)
    except Exception as e:
        print(e)
        continue

    # 创建新的进程
    pid = os.fork()
    if pid == 0:
        # 子进程要处理具体的客户端请求
        s.close()  # 对子进程来说s没用
        handle(c)  # 具体处理请求的函数
        os._exit(0)  # 子进程处理请求后销毁
    else:
        c.close()  # 对父进程来说c没用 不需要和客户端沟通
