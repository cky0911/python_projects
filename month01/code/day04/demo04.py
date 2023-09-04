"""
    str 字面值
    单引和双引号的区别:
        单引号内的双引号不算结束符
        双引号内的单引号不算结束符
    三引号作用:
        换行会自动转换为换行符\n
        三引号内可以包含单引号和双引号
        作为文档字符串
"""
"""
    str字面值
    转义符：改变原始字符含义的特殊符号
"""
# 单引号和双引号 引导的字符串
name1 = "苏大强"
name2 = '苏大强'

# 三引号引导的字符串。独有特点：可见即所得，即打印结果会保持原样
name3 = '''苏大强'''
name4 = """
         苏
        大
        强
"""
print(name4)

# 单引号内的双引号不算结束符
message1 = '我叫"苏大强"。'
# 双引号内的单引号不算结束符
message2 = "我叫'苏大强'。"

"""
    转义符
        1.	改变字符的原始含义。
            \’  \”  \”””  \n  \\  \t  \0 空字符  
        2.	原始字符串：取消转义。
            a = r”C:\newfile\test.py”
"""

# 转义符：\"　\n  \t  \\
message = "我叫\"苏大强\"。"
message = "我叫\n苏大强。"  # 换行
message = "我叫\t苏大强。"  # 水平制表格ｔａｂ键

url = "C:\\nltk_data\\aodels\\bmt15_eval"
# 原始字符串(没有转义符)
url = r"C:\nltk_data\aodels\bmt15_eval"
print(url)

"""
    字符串格式化
        定义：生成一定格式的字符串。
        
        语法：字符串%(变量)
            “我的名字是%s,年龄是%s” % (name, age)
        
        类型码：%s 字符串 %d整数 %f 浮点数
"""
# 字符串格式化
a = "1"
b = "2"
# "请输入" + str(a) + "+" + str(b) + "=?"

# 在字符串中插入变量
# 请输入1+2=?
# 字符串拼接（缺点：乱）
str01 = "请输入" + a + "+" + b + "=?"

str02 = "请输入%s+%s=?" % (a, b)

str03 = "请输入%s+%.1f=?" % ("1", 10.5678)
print(str03)