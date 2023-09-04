"""
    练习:随机加法考试
      随机产生两个数字(1--10),
      在控制台中获取两个数相加的结果
      如果用户输入正确得１０分
    　总共３道题，最后输出得分.
    　例如:"请输入8+3=?"   10   不得分
    　　　　"请输入4+3=?"   7   得10分
    　　　　"请输入4+4=?"   8   得10分
          　”总分是20“
"""
import random

score = 0
for item in range(3):
    random_number01 = random.randint(1, 10)
    random_number02 = random.randint(1, 10)
    input_number = int(input("请输入" + str(random_number01) + "+" + str(random_number02) + "=?"))
    if input_number == random_number01 + random_number02:
        score += 10
print("总分：" + str(score))

"""
    # 在控制台中获取一个整数，判断是否为素数。
    # 素数:只能被１和自身整除的正数.
    # 思路：排除法,使用２到当前数字之间的正数判断，如果存在被整除，则不是素数.
    #  判断9：
    #     能否被2　--  8 之间的数字整除,其中3可以，所以不是素数.
    #  判断８:
    #     能否被2　--  7 之间的数字整除,其中2可以，所以不是素数.
    #  判断7:
    #     能否被2　--  6 之间的数字整除,其中没有，所以是素数.
    # 2 3 5 7  11  13 ....
    
    # ---------思考过程----------------
    # 假设判断11
    # 　　　2  -- 10 之间的数字整除
    
    # if 11 % 2 == 0:
    # print("不是素数")
    
    # if 11 % 3 == 0:
    # print("不是素数")
    
    # if 11 % 4 == 0:
    # print("不是素数")`
"""
number = int(input("请输入一个需要判断是否位素数的整数："))
for num in range(2, number):
    if number % num == 0:
        print("不是素数！")
        break
else:
    print("是素数！")

# 笔记上的
# 备注：没有判断２以下的数字
number = int(input("请输入整数:"))
# 判断2 到number之间的数字，能否整除number.
if number <= 1:
    print("不是素数！")
else:
    for item in range(2, number):  # 2 3 4 5 ...
        if number % item == 0:
            print("不是素数")
            break  # 如果发现满足条件的数字，就不再判断后面的了。
    else:
        print("是素数")
