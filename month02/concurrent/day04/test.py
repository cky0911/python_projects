"""
    测试用例：用于测试进程线程和单进程的执行效率

"""


# 计算
def count(x, y):
    c = 0
    while c < 7000000:
        x += 1
        y += 1
        c += 1


# IO 测试该方法单进程执行10次  创建10个进程   10个线程执行一遍
def io():
    write()
    read()


def write():
    f = open('test', 'w')
    for i in range(2000000):
        f.write("hello world\n")
    f.close()


def read():
    f = open('test')
    lines = f.readlines()
    f.close()
