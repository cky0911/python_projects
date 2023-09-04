# 练习1: 在控制台中循环录入字符串，输入空字符停止.
#       打印所有不重复的文字

set_result = set()
while True:
    str_input = input("请输入：")
    if str_input == "":
        break
    set_result.add(str_input)

print(set_result)

# 练习2: 经理：曹操,刘备,孙权
#       技术：曹操,刘备,张飞,关羽
# 请计算：
#      (1)是经理也是技术的有谁？
#      (2)是经理，不是技术的有谁?
#      (3)是技术，不是经理的有谁?
#      (4)张飞是经理吗?
#      (5)身兼一职的都有谁?
#      (6)经理和技术总共有都少人?
set01 = {"曹操", "刘备", "孙权"}
set02 = {"曹操", "刘备", "张飞", "关羽"}
print(set01 & set02)
print(set01 - set02)
print(set02 - set01)
print("张飞" in set01)
print(set01 ^ set02)
print(len(set01 | set02))
