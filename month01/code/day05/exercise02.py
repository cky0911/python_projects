"""
    练习１：
    在控制台中录入，西游记中你喜欢的人物.
    输入空字符串，打印(一行一个)所有人物.
"""
list_person = []
# 录入过程
while True:
    str_input = input("输入在西游记中喜欢的人物:")
    if str_input == "":
        break
    list_person.append(str_input)

# 输出过程
for item in list_person:
    print(item)

'''
# 练习:在控制台中录入，所有学生成绩.
# 输入空字符串，打印(一行一个)所有成绩.
# 打印最高分,打印最低分,打印平均分.
'''
list_score = []
# 录入过程
while True:
    str_score = input("请输入成绩：")
    if str_score == "":
        break
    list_score.append(int(str_score))
# 输出过程
for item in list_score:
    print(item)

print("最高分：" + str(max(list_score)))
print("最低分：" + str(min(list_score)))
print("平均分：" + str(sum(list_score) / len(list_score)))

"""
# 练习3：
# 在控制台中录入，所有学生姓名.
# 如果姓名重复，则提示"姓名已经存在",不添加到列表中.
# 如果录入空字符串，则倒叙打印所有学生.
"""
list_name = []
while True:
    name = input("请输入姓名:")
    if name == "":
        break
    # 判断变量在列表中是否存在
    if name not in list_name:
        list_name.append(name)
    else:
        print("姓名已经存在")

# -1  -2  -3
# 2  1   0
for item in range(-1, -len(list_name) - 1, -1):
    print(list_name[item])
