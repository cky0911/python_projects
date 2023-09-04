"""
    存储全国各个城市的景区与美食(不用录入),在控制台中显示出来.
  　北京：
        景区：故宫,天安门,天坛.
        美食: 烤鸭,炸酱面,豆汁,卤煮.
    四川:
        景区：九寨沟,峨眉山,春熙路．
        美食: 火锅,串串香,兔头.
"""
dict_place = {
    '北京':
        {
            '景区': ['故宫', '天安门', '天坛'],
            '美食': ['烤鸭', '炸酱面', '豆汁', '卤煮']
        },
    '四川':
        {
            '景区': ['九寨沟', '峨眉山', '春熙路'],
            '美食': ['火锅', '串串香', '兔头']
        }
}

# 需求:获取四川的所有美食
print(dict_place["四川"]["美食"])

# 需求:获取所有城市
for key in dict_place:
    print(key)

# 需求：所有城市的景区
# print(dict01["四川"]["景区"])
# print(dict01["北京"]["景区"])
# print(dict01["xxx"]["景区"])

list02 = []
# 遍历大字典，获取的是地区
for key in dict_place:
    # 遍历景区列表
    for item in dict_place[key]["景区"]:
        # 地区+景区
        list02.append(key + ":" + item)
print(list02)

for key_place, value_place in dict_place.items():
    print('%s：' % key_place)
    for key_play, value_play in value_place.items():
        print('\t%s：' % key_play, end='')
        for i in value_play:
            print(i, end='，')
        print()
