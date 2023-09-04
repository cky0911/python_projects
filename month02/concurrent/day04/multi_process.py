from test import *
from multiprocessing import Process
import time

if __name__ == '__main__':
    jobs = []

    tm = time.time()
    for i in range(10):
        t = Process(target=count, args=(1, 1))
        # t = Process(target=io)
        jobs.append(t)
        t.start()
    for i in jobs:
        i.join()
    print("Process cpu:", time.time() - tm)
