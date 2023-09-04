"""
    练习1:定义计算四位整数，每位相加和的函数.
    测试："1234"   "5428"
"""


def each_unit_sum(number):
    """
        计算整数的每位相加和
    :param number: 四位整数
    :return: 相加的结果
    """
    result = number % 10
    result += number // 10 % 10
    result += number // 100 % 10
    result += number // 1000
    return result


# 测试
re01 = each_unit_sum(1234)
print(re01)
re01 = each_unit_sum(4875)
print(re01)

'''
    # 练习2:定义根据两,计算几斤零几两的函数
    # weight_liang = int(input("请输入两："))
    # jin = weight_liang // 16
    # liang = weight_liang % 16
    # print(str(jin) + "斤零" + str(liang) + "两")
'''


def get_weight_for_jin(liang_weight):
    """
        根据两,计算几斤零几两.
    :param liang_weight:需要计算的两
    :return: 元组 (斤,两)
    """
    jin = liang_weight // 16
    liang = liang_weight % 16
    return (jin, liang) # 返回元组


re = get_weight_for_jin(100)
print(str(re[0]) + "斤零" + str(re[1]) + "两")

"""
    pycharm函数相关快捷键
        “代码自动完成”时间延时设置
        File -> Settings -> Editor -> General -> Code Completion -> Autopopup in (ms):0
    快捷键：
        Ctrl + P 参数信息（在方法中调用参数）
        Ctrl + Q 快速查看文档
        Ctrl + Alt + M 提取方法
"""