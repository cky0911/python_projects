import redis

'''
    寻找活跃用户, >=100次为活跃用户
'''
r = redis.Redis(host='127.0.0.1', port=6379, db=0)

# 模拟4个用户,user001 - user004
# user001: 第1天和第50天登录
r.setbit('user001', 0, 1)
r.setbit('user001', 49, 1)
# user002: 第20天登录1次
r.setbit('user002', 19, 1)
# user003: 一年登录100次以上
for i in range(0, 365, 2):
    r.setbit('user003', i, 1)
# user004: 一年登录100次以上
for i in range(0, 365, 3):
    r.setbit('user004', i, 1)

user_list = r.keys('user*')
active_users = []
inactive_users = []

for user in user_list:
    number = r.bitcount(user)
    if number >= 100:
        active_users.append((user.decode(), number))
    else:
        inactive_users.append((user.decode(), number))

print('活跃用户:', active_users)
print('非活跃用户:', inactive_users)
