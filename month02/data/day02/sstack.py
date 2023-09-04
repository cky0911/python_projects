"""
    sstack.py  栈模型的顺序存储
    重点代码

    思路 :
    1. 顺序存储可以使用列表实现,但是列表功能丰富,不符合栈模型要求
    2. 将列表功能封装,实现顺序栈的类,只提供栈的操作功能

    功能: 出栈, 入栈,判断栈空,查看栈顶元素
"""


# 自定义异常
class StackError(Exception):
    pass


# 顺序栈
class SStack:
    def __init__(self):
        # 空列表就是栈的存储空间
        # 列表的最后一个元素作为栈顶元素
        self.__elems = []
        self.__count = 0

    # 入栈
    def push(self, val):
        self.__elems.append(val)
        self.__count += 1

    # 判断栈空
    def is_empty(self):
        # return self.__elems == []
        return self.__count == 0

    # 出栈
    def pop(self):
        if self.is_empty():
            raise StackError("pop from empty stack")
        self.__count -= 1
        return self.__elems.pop()

    # 查看栈顶
    def top(self):
        if self.is_empty():
            raise StackError("pop from empty stack")
        return self.__elems[-1]

    def get_count(self):
        return self.__count


if __name__ == '__main__':
    st = SStack()
    st.push(10)
    print("get count: %d" % st.get_count())
    st.push(20)
    print("get count: %d" % st.get_count())
    st.push(30)
    print("get count: %d" % st.get_count())
    while not st.is_empty():
        print(st.pop())
        print("get count: %d" % st.get_count())
    # st.pop()

"""
    入栈顺序为1 2 3, 可以随时入随时出， 那么出栈不可能是什么？
    答：不可能是3 1 2, 其他皆有可能
"""