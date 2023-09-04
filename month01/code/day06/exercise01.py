"""
    计算列表中最小值(不使用min)
"""
import random

list01 = [43, 54, 5]
min_value = list01[0]
for i in range(1, len(list01)):
    if min_value > list01[i]:
        min_value = list01[i]
print(min_value)

"""
    4. 彩票　双色球：
    红球:6个，1 -- 33 之间的整数   不能重复
    蓝球:1个，1 -- 16 之间的整数
    (1) 随机产生一注彩票[6个红球１个蓝球].
"""

list_ticket = []
# ６个不重复的红球
while len(list_ticket) < 6:
    random_number = random.randrange(1, 33)
    # 如果随机数不存在，则存储。
    if random_number not in list_ticket:
        list_ticket.append(random_number)
# 1个蓝球
list_ticket.append(random.randrange(1, 16))

print(list_ticket)

"""
    (2) 在控制台中购买一注彩票
    提示：
        "请输入第1个红球号码："
        "请输入第2个红球号码："
        "号码不在范围内"
        "号码已经重复"
        "请输入蓝球号码："
"""
# ６个1--33范围内的不重复红球号码
list_ticket = []
while len(list_ticket) < 6:
    number = int(input("请输入第%d个红球号码:" % (len(list_ticket) + 1)))
    if number < 1 or number > 33:
        print("号码不在范围内")
    elif number in list_ticket:
        print("号码已经重复")
    else:
        list_ticket.append(number)

# １个1--16范围内的蓝球号码
while len(list_ticket) < 7:
    number = int(input("请输入蓝球号码:"))
    if 1 <= number <= 16:
        list_ticket.append(number)
    else:
        print("号码不在范围内")

print(list_ticket)
