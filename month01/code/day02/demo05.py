"""
    bool
    运算符
        比较运算符
        逻辑运算符
"""

"""
    闰年Ｔｒｕｅ:年份能被4整除，但是不能被100整除。
    能被400整除
    平年Ｆａｌｓｅ
"""
year = int(input("请输入年份："))
result = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
print(result)
