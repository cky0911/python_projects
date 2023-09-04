"""
    循环语句
    while 条件:
        满足条件执行的语句
    else:
        不满足条件执行的语句

    else子句可以省略。
    在循环体内用break终止循环时，else子句不执行。
"""
while True:
    usd = int(input("请输入美元："))
    print(usd * 6.9)
    if input("输入q键退出:"):
        break  # 退出循环体

while True:
    season = input("请输入季度：")
    if season == "春":
        print("１月２月３月")
    elif season == "夏":
        print("４月５月６月")
    elif season == "秋":
        print("７月８月９月")
    elif season == "冬":
        print("１０月１１月１２月")

    if input("输入e键退出:") == "e":
        break

count = 0
while count < 3:  # 0  1  2
    count += 1
    usd = int(input("请输入美元："))
    print(usd * 6.9)

# 练习1:在控制台中输出0 1 2 3 4 5
# 练习2:在控制台中输出2 3 4 5 6 7
# 练习3:在控制台中输出0 2 4 6


count = 0
while count < 6:
    print(count)
    count += 1

count = 2
while count < 8:
    print(count)
    count += 1

count = 0
while count <= 6:
    print(count)
    count += 2
