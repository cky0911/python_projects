"""
    使用元组优化代码
        元组作用:
            1. 元组与列表都可以存储一系列变量，由于列表会预留内存空间，所以可以增加元素。
            2. 元组会按需分配内存，所以如果变量数量固定，建议使用元组，因为占用空间更小。
            3. 应用：
                变量交换的本质就是创建元组：x, y = y, x
                格式化字符串的本质就是创建元组：“姓名:%s, 年龄:%d” % (“tarena”, 15)
"""

"""
    练习:借助元组完成下列功能.
"""
# month = int(input("请输入月份："))
#
# if month < 1 or month > 12:
#     print("输入有误")
# elif month == 2:
#     print("２８天")
# elif month == 4 or month == 6 or month == 9\
#         or month == 11:
#     print("３０天")
# else:
#     print("３１天")

# 方式１：
# month = int(input("请输入月份："))
#
# if month < 1 or month > 12:
#     print("输入有误")
# elif month == 2:
#     print("２８天")
# elif month in (4,6,9,11):
#     print("３０天")
# else:
#     print("３１天")

# 方式2:
month = int(input("请输入月份："))
if month < 1 or month > 12:
    print("输入有误")
else:
    # 将每月天数存入元组
    day_of_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    print(day_of_month[month - 1])
