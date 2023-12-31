"""
    select tcp 服务
    重点代码

    思路分析:
    1. 将关注的 IO 放入监控列表
    2. 当 IO 就绪时通知 select 返回
    3. 遍历返回值列表，处理就绪的 IO
"""

from socket import *
from select import select

# 创建监听套接字
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 8888))
s.listen(5)

# 设置关注的IO列表
rlist = [s]  # s用于等待处理连接
wlist = []
xlist = []

# 循环ＩＯ监控
while True:
    # print("++++",rlist)
    rs, ws, xs = select(rlist, wlist, xlist)
    # print('----',rs)
    # 遍历返回值列表，判断哪个ＩＯ就绪
    for r in rs:
        if r is s:
            c, addr = r.accept()
            print("Connect from", addr)
            rlist.append(c)  # 增加新的关注的ＩＯ
        # 不是s就是c了
        else:
            # 表明有客户端发送消息
            data = r.recv(1024).decode()
            # 客户端退出
            if not data:
                # 取消对客户端监控
                rlist.remove(r)
                r.close()
                continue
            print(data)
            # r.send(b'OK')
            wlist.append(r)

    for w in ws:
        w.send(b'OK')
        # 发完消息要移除
        wlist.remove(w)

    for x in xs:
        pass
