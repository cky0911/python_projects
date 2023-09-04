"""
    # 列表排序(升序小　-->  大)
    # [3,80,45,5,7,1]
"""
list_sort = [3, 80, 45, 5, 7, 1]
for i in range(len(list_sort)):
    for j in range(len(list_sort) - 1):
        if list_sort[j] > list_sort[j + 1]:
            list_sort[j], list_sort[j + 1] = list_sort[j + 1], list_sort[j]
print(list_sort)

"""
    练习:
    判断列表中元素是否具有相同的[3,80,45,5,80,1]
    思路：所有元素俩俩比较,发现相同的则打印结果
    　　　所有元素比较结束，都没有发现相同项，则打印结果.
"""
list_same = [3, 80, 45, 5, 80, 1, 5]
list_res = []
for i in range(len(list_same) - 1):
    for j in range(i + 1, len(list_same)):
        if list_same[i] == list_same[j]:
            list_res.append(list_same[i])
print(list_res)

'''
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
    
    # 练习1:打印第二行第三个元素  
    # 练习2:打印第三行每个元素
    # 练习3:打印第一列每个元素
'''
list01 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]
print(list01[1][2])

for item in list01[2]:
    print(item)

# 00  10  20  30    [行索引][列索引]
for r in range(len(list01)):
    print(list01[r][0])

'''
    # 练习:矩阵转置  将二维列表的列，变成行，形成一个新列表.
    #   第一列变成第一行
    #   第二列变成第二行
    #   第三列变成第三行
'''
list_origin = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]
list_res = []
for i in range(len(list_origin)):
    list_temp = []
    for j in range(len(list_origin)):
        list_temp.append(list_origin[j][i])
    list_res.append(list_temp)
print(list_res)

# 参考
# result = []
# for c in range(len(list01[0])):
#     result.append([])
#     for r in range(len(list01)):
#         result[c].append(list01[r][c])
#
# print(result)
