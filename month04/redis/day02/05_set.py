import redis

r = redis.Redis(host='localhost', port=6379, db=0)

r.sadd('ni_tian_xie_shen', 'yun_che', 'xiao_che', 'xia_qing_yue', 'chu_yue_chan', 'mo_li')

result = r.smembers('ni_tian_xie_shen')
print(result)
print(r.scard('ni_tian_xie_shen'))
print(r.sismember('ni_tian_xie_shen', 'mo_li'))

# 创建空集合
r_set = set()
for res in result:
    r_set.add(res.decode())

r.sadd('ni_tian_xie_shen2', 'yun_che', 'xiao_che')

r.sinterstore('inter_set', 'ni_tian_xie_shen', 'ni_tian_xie_shen2')
print(r.smembers('inter_set'))
print('共同好友数:', r.scard('inter_set'))

r.sadd('ni_tian_xie_shen3', 'xiao_che', 'lan_xue_nuo')
print(r.sinter('ni_tian_xie_shen', 'ni_tian_xie_shen2', 'ni_tian_xie_shen3'))
print(r.sunion('ni_tian_xie_shen', 'ni_tian_xie_shen2', 'ni_tian_xie_shen3'))