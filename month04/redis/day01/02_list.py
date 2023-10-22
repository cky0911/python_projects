import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0)
# 列表操作
r.rpush('char_list', 'A', 'E', 'I', 'O', 'U')
r.rpush('char_list', 'Z')

r.linsert('char_list', 'after', 'A', 'B')

print(r.llen('char_list'))

print(r.lrange('char_list', 0, -1))

print(r.rpop('char_list'))

r.ltrim('char_list', 0, 2)

while True:
    result = r.brpop('char_list', 3)
    if not result:
        break
    print(result)

r.expire('char_list', 10)
