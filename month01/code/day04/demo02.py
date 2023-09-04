"""
    continue
"""
# 　累加1--100之间,能被５整除的数字
sum_value = 0
for item in range(1, 101):
    # 满足条件则累加
    if item % 5 == 0:
        sum_value += item
print(sum_value)

sum_value = 0
for item in range(1, 101):
    # 不满足条件则跳过本次循环,继续下次循环。
    if item % 5 != 0:
        continue
    sum_value += item
print(sum_value)

# 累加10-50之间个位不是2,5,9的整数.
sum_value = 0
for item in range(10, 51):
    unit = item % 10
    # 个位是2,5,9的整数　则　跳过.
    if unit == 2 or unit == 5 or unit == 9:
        continue
    sum_value += item

print(sum_value)
