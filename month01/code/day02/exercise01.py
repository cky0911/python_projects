"""
    在控制台中，录入一个商品单价。25
    再录入一个数量 2
    最后获取金额，60 计算应该找回多少钱。60 - 25*2
"""
price = input("请输入商品单价：")
price = float(price)
count = int(input("请输入数量："))
money = float(input("请输金额："))

result = money - price * count

print("应该找回：" + str(result))

"""
    在控制台中获取分钟
    再获取小时
    再获取天
    计算总秒数
"""
minute = int(input("请输入分钟："))
hour = int(input("请输入小时："))
day = int(input("请输入天："))
result = minute * 60 + hour * 60 * 60 + day * 24 * 60 * 60
print("总秒数是:" + str(result))

"""
    古代的秤一斤是１６两
        练习：在控制台中获取两，计算是几斤零几两。
　　　   显示几斤零几两
"""
weight_liang = int(input("请输入两："))
jin = weight_liang // 16
liang = weight_liang % 16
print(str(jin) + "斤零" + str(liang) + "两")

"""
    在控制台中录入距离，时间，初速度，计算加速度。
    匀变速直线运动的位移与时间公式：
    加速度　＝　(距离 - 初速度　×　时间) * 2 / 时间平方
"""
distance = float(input("请输入距离："))
time = float(input("请输入时间："))
initial_velocity = float(input("请输入初速度："))
accelerated_speed = (distance - initial_velocity
                     * time) * 2 / time ** 2
print("加速度是：" + str(accelerated_speed))

"""
    在控制台中录入一个四位整数：1234
    计算每位相加和。　　１＋２＋３＋４
    显示结果。10
"""
number = int(input("请输入４位整数："))  # 1234
# 方法１：分别计算出每位，再相加
# 个位 17:00
unit01 = number % 10
# 十位 1234 // 10 -> 123 % 10 -> 3
unit02 = number // 10 % 10
# 百位 1234 // 100 -> 12 % 10 -> 2
unit03 = number // 100 % 10
# 千位
unit04 = number // 1000
result = unit01 + unit02 + unit03 + unit04
print("结果是：" + str(result))

number = int(input("请输入４位整数："))  # 1234
# 方法２：累加每位
# 个位
result = number % 10
# 累加十位
result += number // 10 % 10
# 累加百位
result += number // 100 % 10
# 累加千位
result += number // 1000
print("结果是：" + str(result))
