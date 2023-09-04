"""
    元组：
        定义：
            由一系列变量组成的不可变序列容器。
            不可变是指一但创建，不可以再添加/删除/修改元素。
            元组的基本操作

        元组的基本操作：
            1. 创建空元组：
                元组名 = ()
                元组名 = tuple()

            2. 创建非空元组：
                元组名 = (20,)
                元组名 = (1, 2, 3)
                元组名 = 100,200,300
                元组名 = tuple(可迭代对象)
        获取元素：
            索引、切片

        遍历元组：
            正向：
            for 变量名 in 列表名:
                变量名就是元素
            反向：
            for 索引名 in range(len(列表名)-1,-1,-1):
                元祖名[索引名]就是元素
"""
# 1. 创建元组
# 空
tuple01 = ()

# 具有默认值
tuple02 = (1, 2, 3)

# 列表　--> 元组
tuple05 = tuple(["a", "b"])
print(tuple05)
# 元组　--> 列表
list01 = list(tuple02)
print(list01)

# 如果元组只有一个元素
# tuple02 = (100)
# print(type(tuple02))# int

# 只有一个元素需要加一个逗号
tuple04 = (100,)
print(type(tuple04))  # tuple

# 不能变化 下面错的
# tuple04[0] = 10

# 2. 获取元素（索引  切片）
tuple05 = ("a", "b", "c", "d")
e01 = tuple05[1]
print(type(e01))  # str

e02 = tuple05[-2:]
print(type(e02))  # tuple

# 可以直接将元组赋值给多个变量
tuple06 = (100, 200)
a, b = tuple06
print(a)
print(b)

# 3. 遍历元素
# 正向
for item in tuple06:
    print(item)

# 反向
# 1  0
for i in range(len(tuple06) - 1, -1, -1):
    print(tuple06[i])
