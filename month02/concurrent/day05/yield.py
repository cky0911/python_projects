"""
    协程基本原理的举例
    协程的本质是一个单线程，无法利用计算机的多核资源
"""


def fun():
    print("start")
    yield 1
    print("end")


g = fun()
print(g.__next__())  # next(g)
print(g.__next__())
