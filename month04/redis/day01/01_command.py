import redis

# 1.连接到redis
r = redis.Redis(host='127.0.0.1', port=6379, db=0)
# 2.调用方法
key_list = r.keys('*')
for key in key_list:
    print(key.decode())

print(r.type('name'))

print(r.exists('list01'))

if r.exists('age'):
    r.delete('age')
