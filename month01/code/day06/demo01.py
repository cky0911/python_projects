"""
    列表推导式
        定义：
        使用简易方法，将可迭代对象转换为列表。

        语法：
        变量 = [表达式 for 变量 in 可迭代对象]
        变量 = [表达式 for 变量 in 可迭代对象 if 条件]

        说明:
        如果if真值表达式的布尔值为False,则可迭代对象生成的数据将被丢弃。
"""
# 将list01中所有元素,增加１以后存入list02中.
list01 = [5, 56, 6, 7, 7, 8, 19]
# list02 = []
# for item in list01:
#     list02.append(item + 1)
list02 = [item + 1 for item in list01]
print(list02)
# 将list01中大于１０元素,增加１以后存入list02中.
# list02 = []
# for item in list01:
#     if item >10:
#         list02.append(item + 1)
list02 = [item + 1 for item in list01 if item > 10]
