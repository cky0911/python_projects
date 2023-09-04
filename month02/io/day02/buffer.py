"""
    buffer.py
    缓冲区刷新测试
    1. 缓冲区满了
    2. 行缓冲换行时会自动刷新
    3. 程序运行结束或文件close关闭
    4. 调用flush()函数
"""

# f = open('a.py','w',1) # 行缓冲
f = open('a.py', 'w')

while True:
    data = input(">>")
    if not data:
        break
    f.write(data + '\n')
    f.flush()  # 刷新缓冲区

f.close()
