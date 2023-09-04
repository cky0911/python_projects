"""
    获取进程PID号
"""

import os
from time import sleep

pid = os.fork()

if pid < 0:
    print("Error")
elif pid == 0:
    sleep(1)  # 出现孤儿进程  父进程挂了 子进程成为孤儿被收养  重要系统不重启 养父进程pid不会改变
    print("Child PID:", os.getpid())  # 子pid
    print("Get parent PID:", os.getppid())  # 父pid
else:
    print("Parent PID:", os.getpid())  # 父pid
    print("Get child PID:", pid)  # 子pid
