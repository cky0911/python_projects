import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0)

while True:
    url = r.brpop('mi:spider', 4)
    if not url:
        print("end of scratch")
        break
    print("scratching!!! please wait...", url[1].decode())
