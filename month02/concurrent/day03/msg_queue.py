"""
    消息队列演示
    注意： 消息存入与去除关系为 先入先出
"""

from multiprocessing import Queue, Process
from time import sleep
from random import randint

# # 创建队列
# q = Queue(5)  # 最大存储5个消息
#
#
# def request():
#     for i in range(10):
#         x = randint(1, 100)
#         y = randint(1, 100)
#         q.put((x, y))  # 写消息队列
#         print("=============")
#
#
# def handle():
#     while not q.empty():
#         data = q.get()  # 读消息队列
#         print("x + y = ", data[0] + data[1])
#         sleep(2)
#
#
# p1 = Process(target=request)
# p2 = Process(target=handle)
# p1.start()
# p2.start()
# p1.join()
# p2.join()

"""
    windows下的演示版本
"""


def request(msg_q):
    for i in range(3):
        x = randint(1, 100)
        y = randint(1, 100)
        msg_q.put((x, y))  # 写消息队列
        print("=============")


def handle(msg_q):
    while not msg_q.empty():
        data = msg_q.get()  # 读消息队列
        print(data)
        print("x + y = ", data[0] + data[1])
        sleep(2)


if __name__ == '__main__':
    msg_q = Queue(5)
    p1 = Process(target=request, args=(msg_q,))
    p2 = Process(target=handle, args=(msg_q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
