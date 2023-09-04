# 练习３:
# 在列表中[54, 25, 12, 42, 35, 17]，选出最大值(不使用max).
list01 = [54, 25, 12, 42, 100, 17]
# 假设第一个是最大的
max_value = list01[0]
# 与后面（从第二个开始）元素进行比较
# 1 2 3 4 5
for i in range(1, len(list01)):
    if max_value < list01[i]:
        # 如果发现更大的，则替换假设的.
        max_value = list01[i]

print(max_value)

"""
    练习４:在列表中[9, 25, 12, 8]，删除大于10的数字
"""
list01 = [9, 25, 12, 8]
for item in list01:
    if item > 10:
        list01.remove(item)
print(list01)
'''
结果为 [9, 12, 8]，12并未被删除
原因在于从左往右删除，被删除的元素的位置会被后面的元素填补，导致填补过来的元素不会被遍历到
内存这样做的目的是提高内存利用率，不然会出现占着茅坑不拉屎
'''

list01 = [9, 25, 12, 8]
# 3 2  1 0
# -1 -2 -3 -4
for i in range(len(list01) - 1, -1, -1):
    if list01[i] > 10:
        list01.remove(list01[i])
print(list01)
