"""
    程序入口
        引入main模块的原因
        main模块是程序的入口
        为提高以后的运行效率，第一次运行程序时，除了main模块外，其他模块都会在pycache文件夹内缓存一份同名的pyc字节码文件
        在做项目开发时，不要把大段代码放到程序最开始运行的那个模块（main）中，这会降低运行效率。
        因此程序入口要保证代码干净、少
"""
from ui import *

view = StudentManagerView()
view.main()
