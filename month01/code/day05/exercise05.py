"""
    练习: 在控制台中循环输入字符串, 如果输入空则停止。
    最后打印所有内容（拼接后的字符串）.
"""

list_result = []
while True:
    str_input = input("请输入：")
    if str_input == "":
        break
    list_result.append(str_input)

str_result = "".join(list_result)
print(str_result)

# 字符串拆分（str–>list）
str01 = "张无忌-赵敏-周芷若"
list_result = str01.split("-")
print(list_result)

# 练习:英文单词翻转
# "How are you" -->"you are How"

str01 = "How are you"
list_temp = str01.split(" ")
str_result = " ".join(list_temp[::-1])
print(str_result)
