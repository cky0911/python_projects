"""
    函数返回值
        一、定义：
            方法定义者告诉调用者的结果。

        二、语法：
            return 数据

        三、说明：
            return后没有语句，相当于返回 None。
            函数体没有return，相当于返回None。
"""
"""
    函数返回值 语法
"""


# 参数：调用者传递给定义者的信息
# 返回值：定义者传递给调用者的结果
def fun01(a):
    print("fun01执行喽")
    # 作用：1. 返回结果  2.退出方法
    return 20
    print("fun01又执行喽")


# F8 逐过程　（调试时跳过方法）
# F7 逐语句  （调试时进入方法）
re = fun01(10)
print(re)


# 无返回值函数
def fun02(a):
    print("fun02执行喽")
    # return None


re = fun02(100)
print(re)
