"""
    thread1.py  线程基础使用
    基本同 Process
    步骤： 1. 封装线程函数
          2. 创建线程对象
          3. 启动线程
          4. 回收线程
"""

import threading
from time import sleep
import os

a = 1


# 线程函数
def music():
    global a
    print("a = ", a)
    a = 10000
    for i in range(3):
        sleep(2)
        print(os.getpid(), "播放: 葫芦娃")


# 线程对象
t = threading.Thread(target=music)
# 启动线程
t.start()

for i in range(4):
    sleep(1)
    print(os.getpid(), "播放: 黄河大合唱")
# 回收线程
t.join()
# join 后分支线程运行完毕
print("===========================")

print("a:", a)
