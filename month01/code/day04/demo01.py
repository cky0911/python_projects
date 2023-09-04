"""
    for语句
    作用：用来遍历可迭代对象的数据元素。

    可迭代对象：指能依次获取数据元素的对象，例如：容器类型。

    语法：
    for 变量列表 in 可迭代对象:
        语句块1
    else:
        语句块2

    说明：else子句可以省略。
    在循环体内用break终止循环时,else子句不执行。
"""
str01 = "我叫苏大强!"

# item 存储的是字符串中每个字符的地址
for item in str01:
    print(id(item))

# 整数生成器:  range(开始值,结束值,间隔)
# for + range ：　更善于执行预定次数。
for item in range(5):  # 01234
    print(item)

# 需求：折纸１０次
thickness = 0.0001
for item in range(10):
    thickness *= 2
print(thickness)
