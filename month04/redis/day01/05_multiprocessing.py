import random
import time
from multiprocessing import Process

import redis


class LianjiaSpider(object):
    def __init__(self):
        self.r = redis.Redis(
            host='127.0.0.1', port=6379, db=0
        )

    # 生产者事件函数 - 生成100个URL,放到redis列表中
    def producer(self):
        for i in range(1, 101):
            url = 'http://lianjia.com/pg{}'.format(i)
            self.r.lpush('lianjia:urls', url)
            time.sleep(random.randint(1, 2))

    # 消费者事件函数 - 获取URL,进行数据抓取
    def consumer(self):
        while True:
            result = self.r.brpop('lianjia:urls', 3)
            if result:
                print('正在抓取:', result[1].decode())
            else:
                break

    # 入口函数
    def run(self):
        p1 = Process(target=self.producer)
        p2 = Process(target=self.consumer)
        p1.start()
        p2.start()
        p1.join()
        p2.join()


if __name__ == '__main__':
    spider = LianjiaSpider()
    spider.run()
