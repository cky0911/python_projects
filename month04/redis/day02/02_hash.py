import redis

r = redis.Redis(host='localhost', port=6379, db=0)

# 设置
r.hset('eng:name', 'name', 'john')
# 更新
r.hset('eng:name', 'name', 'jack')
# 获取
print(r.hget('eng:name', 'name'))

# HGETALL : 字典
print(r.hgetall('eng:name'))
# HKEYS : 列表
print(r.hkeys('eng:name'))
# HVALS : 列表
print(r.hvals('eng:name'))

# 删除field
r.hdel('eng:name', 'gender')
# 删除key
r.delete('eng:name')
