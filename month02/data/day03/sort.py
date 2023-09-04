"""
    sort.py  排序方法训练
"""


def bubble_sort(list_):
    n = len(list_)
    # 外层循环来确定比较多少轮
    for i in range(n - 1):
        # 内存循环确定每轮两两比较多少次
        for j in range(n - 1 - i):
            if list_[j] > list_[j + 1]:
                list_[j], list_[j + 1] = list_[j + 1], list_[j]


# 一轮交换
def sub_sort(list_, low, high):
    # 选定基准
    x = list_[low]
    while low < high:
        # 后面的数向前甩
        while list_[high] > x and high > low:
            high -= 1
        list_[low] = list_[high]  # 将比基准小的数放到前面
        # 前面的数往后甩
        while list_[low] <= x and low < high:
            low += 1
        list_[high] = list_[low]  # 将比基准大的数放到后面
    list_[low] = x  # 将基准数插入
    return low


# 快速排序
def quick_sort(list_, low, high):
    if low < high:
        key = sub_sort(list_, low, high)
        quick_sort(list_, low, key - 1)
        quick_sort(list_, key + 1, high)


list_ = [4, 9, 3, 1, 2, 5, 8, 4]
# bubble_sort(list_)
quick_sort(list_, 0, len(list_) - 1)
print(list_)  # 有序


# 选择排序
def select_sort(list_):
    for i in range(len(list_) - 1):
        min = i
        for j in range(i + 1, len(list_)):
            if list_[min] > list_[j]:
                min = j
        if min != i:
            list_[i], list_[min] = list_[min], list_[i]


select_sort(list_)
print(list_)


# 插入排序
def insert_sort(list_):
    # 控制每次比较的数是那个 从第二个数开始
    for i in range(1, len(list_)):
        x = list_[i]  # 空出list_[i]的位置
        j = i - 1
        while j >= 0 and list_[j] > x:
            list_[j + 1] = list_[j]
            j -= 1
        list_[j + 1] = x


insert_sort(list_)
print(list_)
