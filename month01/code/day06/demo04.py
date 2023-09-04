"""
    字典
        定义:
            由一系列键值对组成的可变映射容器。
            映射：一对一的对应关系，且每条记录无序。
            键必须唯一且不可变(字符串/数字/元组)，值没有限制。
"""

"""
    字典的基本操作:
        一、创建字典：
            字典名 = {键1：值1，键2：值2}
            字典名 = dict (可迭代对象)
        
        二、添加/修改元素：
            语法:
            字典名[键] = 数据
            说明:
            键不存在，创建记录。
            键存在，修改映射关系。
        
        三、获取元素：
            变量 = 字典名[键] # 没有键则错误
            
        四、遍历字典：
            for 键名 in 字典名:
                字典名[键名]
                
        五、删除元素：
            del 字典名[键]
"""
# 1. 创建
# 空
dict01 = {}
dict01 = dict()
# 默认值
dict01 = {"wj": 100, "zm": 80, "zr": 90}
dict01 = dict([("a", "b"), ("c", "d")])
print(dict01)

# 2.　查找元素(根据ｋｅｙ查找ｖａｌｕｅ)
print(dict01["a"])
# 如果ｋｅｙ不存在，查找时会错误.
if "qtx" in dict01:  # 如果存在key
    print(dict01["qtx"])

# 3.　修改元素(之前存在ｋｅｙ)
dict01["a"] = "BB"

# 4. 添加(之前不存在ｋｅｙ)
dict01["e"] = "f"

# 5. 删除
del dict01["a"]

print(dict01)
# 6. 遍历（获取字典中所有元素）

# 遍历字典，获取key
for key in dict01:
    print(key)
    print(dict01[key])

# 遍历字典，获取value
for value in dict01.values():
    print(value)

# 遍历字典，获取键值对key value(元组).
# for item in dict01.items():
#     print(item[0])
#     print(item[1])

for k, v in dict01.items():
    print(k)
    print(v)
    # print("key : %s value : %s" % (k, v))
