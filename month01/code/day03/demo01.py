"""
    del
        语法:
        del 变量名1, 变量名2

        作用:
        用于删除变量,同时解除与对象的关联.如果可能则释放对象。

        延伸：自动化内存管理的引用计数
        每个对象记录被变量绑定(引用)的数量，当数量为0时对象会被销毁。
"""

a = "悟空"
b = a
c = a
# 删除变量a,b,不释放对象"悟空"
del a, b
# 由于变量ｃ不再引用对象"悟空",而悟空的引用计数为０，所以被标记为可回收。
c = None
