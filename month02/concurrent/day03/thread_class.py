"""
    自定义线程类示例
"""

from threading import Thread


# 自定义线程类
class ThreadClass(Thread):
    # 重写父类init
    def __init__(self, value):
        self.value = value
        # 加载父类init
        super().__init__()

    def f1(self):
        print("步骤1")

    def f2(self):
        print("步骤2")

    # 作为流程启动函数
    def run(self):
        for i in range(self.value):
            self.f1()
            self.f2()


if __name__ == '__main__':
    t = ThreadClass(2)
    t.start()
    t.join()
