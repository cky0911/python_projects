"""
    练习1:在控制台中循环录入商品信息(名称,单价).
    　　　如果名称输入空字符,则停止录入.
         将所有信息逐行打印出来.
"""
dict_commodity_info = {}
while True:
    name = input("请输入商品名称：")
    if name == "":
        break
    price = int(input("请输入商品单价："))
    dict_commodity_info[name] = price

for key, value in dict_commodity_info.items():
    print("%s商品单价是%d" % (key, value))

# 键存在 值覆盖

"""
    练习2: 在控制台中循环录入学生信息(姓名,年龄,成绩,性别).
     　　　如果名称输入空字符, 则停止录入.
           将所有信息逐行打印出来.
"""
"""
    # 字典内嵌列表:
    {
        "张无忌":[28,100,"男"],
    }
"""
dict_student_info = {}
while True:
    name = input("请输入姓名：")
    if name == "":
        break
    age = int(input("请输入年龄："))
    score = int(input("请输入成绩："))
    sex = input("请输入性别：")
    dict_student_info[name] = [age, score, sex]

# 打印所有学生信息
for name, list_info in dict_student_info.items():
    print("%s的年龄是%d,成绩是%d,性别是%s" % (name, list_info[0], list_info[1], list_info[2]))

"""
    # 字典内嵌字典:
    {
        "张无忌":{"age":28,"score":100,"sex":"男"},
    }
"""
dict_student_info = {}
while True:
    name = input("请输入姓名：")
    if name == "":
        break
    age = int(input("请输入年龄："))
    score = int(input("请输入成绩："))
    sex = input("请输入性别：")
    dict_student_info[name] = {"age": age, "score": score, "sex": sex}

for name, dict_info in dict_student_info.items():
    print("%s的年龄是%d,成绩是%d,性别是%s" % (name, dict_info["age"], dict_info["score"], dict_info["sex"]))

"""
    # 列表内嵌字典:
    [
        {"name":"张无忌","age":28,"score":100,"sex":"男"},
    ]
"""
list_student_info = []
while True:
    name = input("请输入姓名：")
    if name == "":
        break
    age = int(input("请输入年龄："))
    score = int(input("请输入成绩："))
    sex = input("请输入性别：")
    dict_info = {"name": name, "age": age, "score": score, "sex": sex}
    list_student_info.append(dict_info)

for dict_info in list_student_info:
    print(
        "%s的年龄是%d,成绩是%d,性别是%s" % (dict_info["name"], dict_info["age"], dict_info["score"], dict_info["sex"]))
# 获取第一个学生信息
dict_info = list_student_info[0]
print("第一个录入的是：%s,年龄是%d,成绩是%d,性别是%s" % (
    dict_info["name"], dict_info["age"], dict_info["score"], dict_info["sex"]))
