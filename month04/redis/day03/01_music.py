import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0)
# 1.在有序集合中添加几首歌曲,播放次数为1
r.zadd('ranking', {'song1': 1, 'song2': 1, 'song3': 1})
r.zadd('ranking', {'song4': 1, 'song5': 1, 'song6': 1})
r.zadd('ranking', {'song7': 1, 'song8': 1, 'song9': 1})
# 2.播放部分歌曲
r.zincrby('ranking', 30, 'song1')
r.zincrby('ranking', 50, 'song6')
r.zincrby('ranking', 80, 'song8')
# 3.获取前3名
# result: [(b'song8', 81.0), (b'song6', 51.0), (b'song1', 31.0)]
result = r.zrevrange('ranking', 0, 2, withscores=True)
i = 1
for name in result:
    print('第{}名:{} 播放次数:{}'.format(
        i, name[0].decode(), int(name[1])
    ))
    i += 1
