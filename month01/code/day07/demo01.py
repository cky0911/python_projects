"""
    字典推导式
        定义：
            使用简易方法，将可迭代对象转换为字典。
        语法:
            {键:值 for 变量 in 可迭代对象}
            {键:值 for 变量 in 可迭代对象 if 条件}
"""
# 1 2 3 4 ... 10 -> 平方
dict01 = {}
for item in range(1, 11):
    dict01[item] = item ** 2
print(dict01)
# 推导式:
dict02 = {item: item ** 2
          for item in range(1, 11)}
print(dict02)

# 只记录大于５的数字
dict01 = {}
for item in range(1, 11):
    if item > 5:
        dict01[item] = item ** 2

print(dict01)

dict02 = {item: item ** 2 for item in range(1, 11) if item > 5}
print(dict02)
