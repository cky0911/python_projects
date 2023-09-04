# 练习1:从列表[4,5,566,7,8,10]中选出所有偶数
# -- 结果存入另外一个列表中
# -- 使用生成器实现

list01 = [4, 5, 566, 7, 8, 10]


# 遍历列表实现
def get_even01():
    result = []
    for item in list01:
        if item % 2 == 0:
            result.append(item)
    return result


re = get_even01()
for item in re:
    print(item)


# 使用生成器实现
def get_even02():
    for item in list01:
        if item % 2 == 0:
            # yield 离不开函数
            yield item  # 方法要返回多个结果的情况下使用yield方便


# 直接调用不会进去
g01 = get_even02()  # 这行打断点F7
for item in g01:
    print(item)
