# 练习:将下列代码，定义到函数中，再调用一次.
def print_rectangle(r_count, c_count, char):
    """
        打印矩形
    @param r_count: 行数
    @param c_count: 列数
    @param char: 填充的字符　
    """
    for r in range(r_count):
        # 内层循环控制列　
        for c in range(c_count):
            print(char, end=" ")
        print()


print_rectangle(5, 2, "#")


# 练习:定义在控制台中打印一维列表的函数.
# 例如：[1,2,3]-->1 2 3  每个元素一行

def print_list(list_target):
    """
        打印列表
    :param list_target: 目标列表　
    """
    for item in list_target:
        print(item)


list01 = [1, 2, 3]
list02 = ["a", True, 1.5, 10]

print_list(list02)
