"""
    进程对象属性
"""

from multiprocessing import Process
import time


def tm():
    for i in range(3):
        print(time.ctime())
        time.sleep(2)


if __name__ == "__main__":
    # name 进程名称
    p = Process(target=tm, name='process_me')

    # 父进程退出，其所有子进程也退出  daemon 不会与join一起使用
    # p.daemon = True

    p.start()  # 进程真正产生

    print("Name:", p.name)  # 进程名
    print("PID：", p.pid)  # pid号
    print("is alive:", p.is_alive())  # 是否在生命周期
