import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0)

# python 操作 string
r.set('user001:name', 'zhangsan')
m_dict = {
    'user001:age': 22,
    'user001:gender': 'm'
}

r.mset(m_dict)
print(r.get('user001:name'))
print(r.mget('user001:age', 'user001:gender'))
print(r.strlen('user001:name'))


r.incr('user001:age')
print(r.get('user001:age'))
r.decr('user001:age')
print(r.get('user001:age'))
r.incrby('user001:age', 2)
print(r.get('user001:age'))
