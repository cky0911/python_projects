import redis
import pymysql

# 1.先到redis中查询
# 2.redis中没有,到mysql中查询
# 3.再缓存到redis中一份,设置过期时间30秒
# 4.再查一遍
r = redis.Redis(host='localhost', port=6379, db=0)
# 连接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='user_db',
                     charset='utf8')
cursor = db.cursor()
# 开始 - 用户点击查询个人信息
username = input('请输入用户名:')
# redis查询
result = r.hgetall(username)
if result:
    print('redis:', result)
else:
    # redis中没有,需要到mysql中查询
    sel = 'select age, gender, score from user where name=%s'
    cursor.execute(sel, [username])
    user_info = cursor.fetchall()
    if not user_info:
        print("user not exists!!!")
    else:
        print('mysql:', user_info)
        # user_info: ((25, 'M', 99),)
        # 缓存到redis一份
        r.hset(username, 'age', user_info[0][0])
        r.hset(username, 'gender', user_info[0][1])
        r.hset(username, 'score', user_info[0][2])
        # 设置过期时间
        r.expire(username, 30)
