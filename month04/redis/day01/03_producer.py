import redis
import time
import random

r = redis.Redis(host='127.0.0.1', port=6379, db=0)

# 生产URL
for page in range(67):
    url = 'http://api.mi.com/category/2#page={}'.format(page)
    r.lpush('mi:spider', url)
    time.sleep(random.randint(1, 3))
