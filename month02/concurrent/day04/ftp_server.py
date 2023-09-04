"""
    ftp 文件服务器 ,服务端
    多进程/多线程并发 socket
    功能
        【1】 分为服务端和客户端，要求可以有多个客户端同时操作。
        【2】 客户端可以查看服务器文件库中有什么文件。
        【3】 客户端可以从文件库中下载文件到本地。
        【4】 客户端可以上传一个本地文件到文件库。
        【5】 使用print在客户端打印命令输入提示，引导操作
"""

import os
import sys
import time
from socket import *
from threading import Thread

# 全局变量
ADDR = ('127.0.0.1', 8080)
# 文件库路径
# FTP = r'D:\develop\PyProjects\ftp_test'
FTP = "D:/develop/PyProjects/ftp_test/"


# 功能类 (线程类)
# 查列表, 下载, 上传
class FTPServer(Thread):
    def __init__(self, connfd):
        super().__init__()
        self.connfd = connfd

    # 处理文件列表
    def do_list(self):
        # 获取文件列表
        files = os.listdir(FTP)
        if not files:
            self.connfd.send("文件库为空".encode())
            return
        else:
            self.connfd.send(b'OK')
            # 防止粘包
            time.sleep(0.1)
        # 拼接文件
        filelist = ''
        for file in files:
            filelist += file + '\n'
        self.connfd.send(filelist.encode())

    def do_get(self, filename):
        try:
            f = open(FTP + filename, 'rb')
        except Exception:
            # 文件不存在
            self.connfd.send('文件不存在'.encode())
            return
        else:
            self.connfd.send(b'OK')
            time.sleep(0.1)

        # 发送文件
        while True:
            data = f.read(1024)
            if not data:
                time.sleep(0.1)
                self.connfd.send(b'##')
                break
            self.connfd.send(data)

    def do_put(self, filename):
        if os.path.exists(FTP + filename):
            self.connfd.send("文件已存在".encode())
            return
        else:
            self.connfd.send(b'OK')
        # 　接收文件
        f = open(FTP + filename, 'wb')
        while True:
            data = self.connfd.recv(1024)
            if data == b'##':
                break
            f.write(data)
        f.close()

    # 循环接受来自客户端的请求 quit get put list
    def run(self):
        while True:
            request = self.connfd.recv(1024).decode()
            if not request or request == 'Q':
                return  # 线程结束退出
            elif request == 'L':
                self.do_list()
            elif request[0] == 'G':
                filename = request.split(' ')[-1]
                self.do_get(filename)
            elif request[0] == 'P':
                filename = request.split(' ')[-1]
                self.do_put(filename)


# 启动函数 搭建网络服务端模型
def main():
    # 创建监听套接字
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)
    s.listen(5)

    print("Listen the port 8080....")

    while True:
        # 循环等待客户端连接
        try:
            c, addr = s.accept()
            print("Connect from", addr)
        except KeyboardInterrupt:
            sys.exit()
        except Exception as e:
            print(e)
            continue

        # 创建新的线程处理请求
        client = FTPServer(c)
        client.setDaemon(True)
        client.start()


if __name__ == "__main__":
    main()
