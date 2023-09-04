"""
    选择语句：	让程序根据条件选择性的执行语句。
        if 条件1:
        语句块1
        elif 条件2:
            语句块2
        else:
        语句块3

        elif 子句可以有0个或多个。
        else 子句可以有0个或1个，且只能放在if语句的最后。
"""

sex = input("请输入性别：")
if sex == "男":
    print("您好，先生！")
elif sex == "女":
    print("您好，女士！")
else:
    print("性别未知")

print("后续逻辑")
