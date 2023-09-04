"""
    用两个子进程分别拷贝图片的上半部分和下半部分
"""

from multiprocessing import Process
import os

filename = "./timg.png"
size = os.path.getsize(filename)


# 所有进程使用的是同一个IO，相互有影响
# fr = open(filename,'rb')
# print(fr.fileno())

# 复制上半部分
def top():
    fr = open(filename, 'rb')
    print(fr.fileno())
    fw = open('top.png', 'wb')
    n = size // 2
    fw.write(fr.read(n))
    fr.close()
    fw.close()


# 下半部分
def bot():
    fr = open(filename, 'rb')
    print(fr.fileno())
    fw = open('bot.png', 'wb')
    # 以开头为基准 向后移动 size // 2
    fr.seek(size // 2, 0)
    fw.write(fr.read())
    fr.close()
    fw.close()


if __name__ == '__main__':
    p1 = Process(target=top)
    p2 = Process(target=bot)
    p2.start()
    p1.start()
    p1.join()
    p2.join()
