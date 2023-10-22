import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0)

day01_dict = {
    'huawei': 5000,
    'oppo': 4000,
    'iphone': 3000
}
day02_dict = {
    'huawei': 5200,
    'oppo': 4300,
    'iphone': 3230
}
day03_dict = {
    'huawei': 5500,
    'oppo': 4400,
    'iphone': 3600
}

r.zadd('mobile-001', day01_dict)
r.zadd('mobile-002', day02_dict)
r.zadd('mobile-003', day03_dict)

# 并集,第二个参数为元组
r.zunionstore(
    'mobile-001:003',
    ('mobile-001', 'mobile-002', 'mobile-003'),
    aggregate='max'
)
# 逆序:[(),(),()]
rlist = r.zrevrange('mobile-001:003', 0, 2, withscores=True)

for r in rlist:
    print('{}-{}'.format(r[0].decode(), int(r[1])))
