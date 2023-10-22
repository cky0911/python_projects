import redis
import pymysql


# 1.先到mysql更新update更新数据
# 2.缓存到redis中
# 2种情况: (1)redis中之前没有缓存 - 缓存(所有字段)
#         (2)redis中之前缓存过 - 直接更新字段
class Update(object):
    def __init__(self):
        self.db = pymysql.connect(host='localhost',
                                  port=3306,
                                  user='root',
                                  password='123456',
                                  database='user_db',
                                  charset='utf8')
        self.cursor = self.db.cursor()
        self.r = redis.Redis(host='localhost', port=6379, db=0)

    # 更新mysql表记录
    def update_mysql(self, score, username):
        upd = 'update user set score=%s where name=%s'
        try:
            self.cursor.execute(upd, [score, username])
            self.db.commit()
            return True
        except Exception as e:
            self.db.rollback()
            print('Failed', e)

    # 更新redis
    def update_redis(self, username, score):
        result = self.r.hgetall(username)
        # result非空: 更新score字段
        # result为空: 到mysql查询,然后再缓存
        if result:
            self.r.hset(username, 'score', score)
        else:
            self.select_mysql(username)

    def select_mysql(self, username):
        sel = 'select age, gender, score from user where name=%s'
        self.cursor.execute(sel, [username])
        result = self.cursor.fetchall()
        # 同步到redis
        self.r.hset(username, 'age', result[0][0])
        self.r.hset(username, 'gender', result[0][1])
        self.r.hset(username, 'score', result[0][2])
        self.r.expire(username, 30)

    # 主函数
    def main(self):
        username = input('请输入用户名:')
        new_score = input('请输入新成绩:')
        if self.update_mysql(new_score, username):
            self.update_redis(username, new_score)
        else:
            print('更新失败')


if __name__ == '__main__':
    syn = Update()
    syn.main()
