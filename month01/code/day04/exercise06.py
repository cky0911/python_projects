"""
    练习:猜数字游戏
    游戏运行产生一个１－－１００之间的随机数。
    让玩家重复猜测，直到猜对为止。
    提示:大了
    　　　小了
    　　　　猜对了，总共猜了多少次
"""
# 随机数工具(在开头写一次)
import random

# 产生一个随机数
random_number = random.randint(1, 100)
count = 0
while True:
    count += 1
    input_number = int(input("请输入数字："))
    if input_number > random_number:
        print("大了")
    elif input_number < random_number:
        print("小了")
    else:
        print("猜对了，总共猜了" + str(count) + "次")
        break

"""
    循环中的else语句块只有循环正常结束才会执行
    对while循环，也就是 其条件判定不满足之时
"""
"""
import random

random_number = random.randint(1, 100)
print(random_number)
count = 0
while count < 3:
    # 三次以内
    count += 1
    input_number = int(input("请输入数字："))
    if input_number > random_number:
        print("大了")
    elif input_number < random_number:
        print("小了")
    else:
        print("猜对了，总共猜了" + str(count) + "次")
        break  # 退出循环体，不会执行else语句。
else:  # while的条件不满足时，执行
    # 三次以外
    print("失败")
"""
