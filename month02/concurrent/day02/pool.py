"""
    进程池使用
"""
from multiprocessing import *
from time import sleep, ctime


# 进程池事件 要写在创建进程池之前
def worker(msg):
    sleep(2)
    print(ctime(), '--', msg)


if __name__ == '__main__':
    # 创建进程池
    pool = Pool(3)

    # 向进程池队列添加事件
    for i in range(10):
        msg = "add event %d" % i
        pool.apply_async(func=worker, args=(msg,))

    # 关闭进程池
    pool.close()

    # 回收进程池
    pool.join()
