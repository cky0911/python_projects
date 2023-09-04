"""
3.  按照以下格式，输出变量name = "悟空",age = 800,score = 99.5
     我叫xx,年龄是xx,成绩是xx。
"""
name = "悟空"
age = 800
score = 99.5
message = "我叫%s, 年龄是%d, 成绩是%.1f。" % (name, age, score)
print(message)

"""
4.　在控制台中获取一个整数作为边长．
　　根据边长打印矩形．
   例如：４
       ****
       *  *
       *  *
       ****

       6
       ******
       *    *
       *    *
       *    *
       *    *
       ******
"""
number = int(input("请输入整数:"))  # 4

print("*" * number)

for item in range(number - 2):  #
    print("*" + " " * (number - 2) + "*")

print("*" * number)

"""
5.在控制台中录入一个字符串，判断是否为回文．
  判断规则:正向与反向相同．
  　　　上海自来水来自海上
"""
message = "上海自来水来自海上"
if message == message[::-1]:
    print("是回文")
else:
    print("不是回文")

"""
6. (扩展)一个小球从１００ｍ的高度落下
    　　每次弹回原高度的一半．
    　　计算：总共弹起来多少次（最小弹起高度0.01ｍ）．
            总共走了多少米
"""
height = 100
count = 0
# 经过距离
distance = height
# 弹起前高度 大于　最小弹起高度
# while height > 0.01:
# 弹起来的高度 大于　最小弹起高度
while height / 2 > 0.01:
    count += 1
    # 弹起
    height /= 2
    print("第%d次弹起来的高度是%f." % (count, height))
    # 累加起/落高度
    distance += height * 2

print("总共弹起来%d次" % count)
print("总共经过的距离是%.2f" % distance)
