"""
    数据模型类：StudentModel
            数据：编号 id,姓名 name,年龄 age,成绩 score
    逻辑控制类：StudentManagerController
            数据：学生列表 __stu_list
            行为：获取列表 stu_list,添加学生 add_student，删除学生remove_student，
                修改学生update_student，根据成绩排序order_by_score。
    界面视图类：StudentManagerView
            数据：逻辑控制对象__manager
            行为：显示菜单__display_menu，选择菜单项__select_menu_item，入口逻辑main，
                输入学生__input_students，输出学生__output_students，删除学生__delete_student，
                修改学生信息__modify_student，按成绩输出学生__output_student_by_score
"""

"""
    学生管理系统
    项目计划：
        1.完成数据模型类StudentModel
        2.创建逻辑控制类StudentManagerController
        3.完成数据：学生列表 __stu_list
        4.行为：获取列表 stu_list,
        5.添加学生方法 add_student
        6.根据编号删除学生remove_student
        7.根据编号修改学生update_student
        8.在界面视图类中，根据编号删除学生
        9.在界面视图类中，根据编号修改学生
"""


class StudentModel:
    """
        学生模型
    """

    def __init__(self, name="", age=0, score=0, id=0):
        """
           创建学生对象
        :param name: 姓名,str类型.
        :param age: 年龄,int类型
        :param score: 成绩,float类型
        :param id: 编号(该学生对象的唯一标识)
        """
        self.name = name
        self.age = age
        self.score = score
        self.id = id


class StudentManagerController:
    """
        学生管理控制器,负责业务逻辑处理.
    """

    # 类变量,表示初始编号.
    __init_id = 1000

    def __init__(self):
        self.__stu_list = []

    @property
    def stu_list(self):
        """
            学生列表
        :return: 存储学生对象的列表
        """
        return self.__stu_list

    def add_student(self, stu_info):
        """
            添加一个新学生
        :param stu_info: 没有编号的学生信息
        """
        stu_info.id = self.__generate_id()

        self.__stu_list.append(stu_info)

    def __generate_id(self):
        StudentManagerController.__init_id += 1
        return StudentManagerController.__init_id

    def remove_student(self, id):
        """
            根据编号移除学生信息
        :param id: 编号
        :return:
        """
        for item in self.__stu_list:
            if item.id == id:
                self.__stu_list.remove(item)  # 无法用del
                return True  # 表示移除成功
        return False  # 表示移除失败

    def update_student(self, stu_info):
        """
            根据stu_info.id修改其他信息
        :param stu_info: 学生对象
        :return: 是否修改成功
        """
        for item in self.__stu_list:
            if item.id == stu_info.id:
                item.name = stu_info.name
                item.age = stu_info.age
                item.score = stu_info.score
                return True
        return False

    def order_by_score(self):
        """
            根据成绩，对self.__stu_list进行升序排列
        """
        for r in range(len(self.__stu_list) - 1):
            for c in range(r + 1, len(self.__stu_list)):
                if self.__stu_list[r].score > self.__stu_list[c].score:
                    self.__stu_list[r], self.__stu_list[c] = self.__stu_list[c], self.__stu_list[r]


class StudentManagerView:
    """
    学生管理器视图
    """

    def __init__(self):
        # 只做一次
        self.__manager = StudentManagerController()

    def __display_menu(self):
        print("1)添加学生")
        print("2)显示学生")
        print("3)删除学生")
        print("4)修改学生")
        print("5)按照成绩升序显示学生")

    def __select_menu(self):
        item = input("请输入：")
        if item == "1":
            self.__input_student()
        elif item == "2":
            self.__output_students(self.__manager.stu_list)
        elif item == "3":
            self.__delete_student()
        elif item == "4":
            self.__modify_student()
        elif item == "5":
            self.__output_student_by_score()

    def main(self):
        """
            界面视图入口
        :return:
        """
        while True:
            self.__display_menu()
            self.__select_menu()

    def __input_student(self):
        name = input("请输入姓名：")
        age = int(input("请输入年龄："))
        score = int(input("请输入成绩："))
        stu = StudentModel(name, age, score)
        self.__manager.add_student(stu)

    def __output_students(self, list_output):
        for item in list_output:
            print(item.id, item.name, item.age, item.score)

    def __delete_student(self):
        # 注意类型  输入的是字符串
        id = int(input("请输入编号："))
        if self.__manager.remove_student(id):
            print("删除成功")
        else:
            print("删除失败")

    def __modify_student(self):
        stu = StudentModel()
        stu.id = int(input("请输入需要修改的学生编号:"))
        stu.name = input("请输入新的学生名称：")
        stu.age = int(input("请输入新的学生年龄："))
        stu.score = int(input("请输入新的学生成绩："))
        if self.__manager.update_student(stu):
            print("修改成功")
        else:
            print("修改失败")

    def __output_student_by_score(self):
        self.__manager.order_by_score()
        self.__output_students(self.__manager.stu_list)


"""
# 测试添加学生功能
manager = StudentManagerController()
s01 = StudentModel("zs", 24, 100)
manager.add_student(s01)
manager.add_student(StudentModel("ls", 24, 100))

for item in manager.stu_list:
    print(item.id, item.name)
"""

"""
# 测试删除学生
manager = StudentManagerController()
manager.add_student(StudentModel("zs"))
manager.add_student(StudentModel("ls"))
print(manager.remove_student(1001))
for item in manager.stu_list:
    print(item.id, item.name)
"""

"""
# 测试修改学生
manager = StudentManagerController()
manager.add_student(StudentModel("zs"))
for item in manager.stu_list:
    print(item.id, item.name, item.score, item.age)
manager.update_student(StudentModel("张三", 27, 84, 1001))
print("修改后...")
for item in manager.stu_list:
    print(item.id, item.name, item.score, item.age)
"""

# 测试添加和显示
view = StudentManagerView()
view.main()
