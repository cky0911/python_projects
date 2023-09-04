"""
    静态方法
        语法
            (1) 定义：
                @staticmethod
                def 方法名称(参数列表):
                方法体
            (2) 调用：类名.方法名(参数列表)
                不建议通过对象访问静态方法

        说明
            – 使用@ staticmethod修饰的目的是该方法不需要隐式传参数。
            – 静态方法不能访问实例成员和类成员

        作用
            定义常用的工具函数。

"""

list01 = [
    ["00", "01", "02", "03"],
    ["10", "11", "12", "13"],
    ["20", "21", "22", "23"],
]


class Vector2:
    """
        二维向量
        可以表示位置/方向
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y


# 函数:表示左边方向
def left():
    return Vector2(0, -1)


# 函数:表示右边方向
def right():
    return Vector2(0, 1)


# 作用：位置　＋　方向
pos01 = Vector2(1, 2)
l01 = left()
pos01.x += l01.x
pos01.y += l01.y
print(pos01.x, pos01.y)
