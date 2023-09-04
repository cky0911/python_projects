"""
    day07 复习
    能力提升for for
        # 结论：外层循环执行一次，内层循环执行多次。
        　　　　外层控制行，内层控制列.

        for r in range(2):#     0     1
            for c in range(3):#012   012
                pass

    函数
        定义:功能，使用一个名称，包装多个语句。
        语法:
            做
                def 名字(形参):
                    函数体

            用
                名字(实参)
"""
"""
3. 定义在控制台中打印二维列表的函数
[
    [1,2,3,44],
    [4,5,5,5,65,6,87],
    [7,5]
]

1 2 3 44
4 5 5 5 65 6 87
7 5
"""


def print_double_list(double_list):
    """
        打印二维列表
    :param double_list: 需要打印的二维列表
    """
    for line in double_list:
        for item in line:
            print(item, end=" ")
        print()


list01 = [
    [1, 2, 3, 44],
    [4, 5, 5, 5, 65, 6, 87],
    [7, 5]
]
print_double_list(list01)
