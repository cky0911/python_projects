"""
    真值表达式
    条件表达式

    if 数据:
    语句
    本质就是使用bool函数操作数据

      语法：变量 = 结果1 if 条件 else 结果2
     作用：根据条件(True/False) 来决定返回结果1还是结果2。


"""
if 100:
    print("真值")
# 等同于
if bool(100):
    print("真值")

# sex = None
# if input("请输入性别:") == "男":
#     sex = 1
# else:
#     sex = 0
# print(sex)
sex = 1 if input("请输入性别:") == "男" else 0
print(sex)
