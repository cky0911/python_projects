"""
    chat room
    socket udp & fork
"""
import os
from socket import *

# 服务端地址
ADDR = ('0.0.0.0', 8888)
# 存储用户的结构 {name:address}
user = {}


# 处理登录
def do_login(s, name, addr):
    if name in user or '管理员' in name:
        s.sendto("该用户已存在".encode(), addr)
        return

    # 加入用户
    msg = "\n欢迎 %s 进入聊天室" % name
    for i in user:
        s.sendto(msg.encode(), user[i])
    # 插入字典中
    user[name] = addr
    s.sendto(b'OK', addr)


# 聊天
def do_chat(s, name, text):
    msg = "\n%s: %s" % (name, text)
    for i in user:
        # 刨除本人
        if i != name:
            s.sendto(msg.encode(), user[i])


# 退出
def do_quit(s, name):
    msg = "\n%s 退出聊天室" % name
    for i in user:
        # 其他人
        if i != name:
            s.sendto(msg.encode(), user[i])
        else:
            s.sendto(b'EXIT', user[i])
    # 删除该用户
    del user[name]


# 接受请求，分发给不同方法处理
def do_request(s):
    while True:
        # 循环接收来自客户端请求
        data, addr = s.recvfrom(1024)
        # 防止聊天内容存在空格
        tmp = data.decode().split(' ', 2)
        # 根据不同的请求类型分发函数处理；L 进入  C 聊天  Q 退出
        if tmp[0] == 'L':
            do_login(s, tmp[1], addr)
        elif tmp[0] == 'C':
            # text = ' '.join(tmp[2:])
            do_chat(s, tmp[1], tmp[2])
        elif tmp[0] == 'Q':
            if tmp[1] in user:
                do_quit(s, tmp[1])


# 搭建网络
def main():
    # udp服务端
    s = socket(AF_INET, SOCK_DGRAM)
    s.bind(ADDR)

    # 开辟新的子进程处理管理员消息
    pid = os.fork()
    if pid == 0:
        # 子进程处理管理员消息
        while True:
            msg = input("管理员消息:")
            msg = "C 管理员 " + msg
            # 发给自身
            s.sendto(msg.encode(), ADDR)
    else:
        # 处理客户端请求
        do_request(s)


main()
