"""
    在控制台中分别录入４个数字
    打印最大的数字
"""
number01 = float(input("请输入第1个数字："))
number02 = float(input("请输入第2个数字："))
number03 = float(input("请输入第3个数字："))
number04 = float(input("请输入第4个数字："))

# 　假设第一个是最大值
max_value = number01
# 以此与后面进行比较
if max_value < number02:
    # 发现更大的，则替换假设的。
    max_value = number02
if max_value < number03:
    max_value = number03
if max_value < number04:
    max_value = number04
print(max_value)
