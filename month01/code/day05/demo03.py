"""
    列表 VS字符串
        1.列表和字符串都是序列,元素之间有先后顺序关系。
        2.字符串是不可变的序列,列表是可变的序列。
        3.字符串中每个元素只能存储字符,而列表可以存储任意类型。
        4.列表和字符串都是可迭代对象。
        5.函数：
            将多个字符串拼接为一个。
            result = “连接符”.join(列表)
            将一个字符串拆分为多个。
            列表 = “a-b-c-d”.split(“分隔符”)
"""

'''
 需求：根据ｘｘ逻辑，拼接一个字符串.
 "0123456789"
'''

'''
方法一：字符串相加
缺点：每次循环形成（+=）一个新的字符串对象,替换变量引用result。
'''
result = ""
for item in range(10):
    # ""
    # "0"
    # "01"
    # "012"
    result = result + str(item)
print(result)

'''
方法二：列表，join()
优点：每次循环只向列表添加字符串，没有创建列表对象。
'''
list_temp = []
for item in range(10):
    list_temp.append(str(item))
# join : list --> str
result = " ".join(list_temp)
print(type(result))
print(result)
