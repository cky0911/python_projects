## 阶段一
### day01
- 输入、输出、快捷键
### day02
- 变量、数据类型、数据类型转换、运算符
### day03
- 身份运算符、选择语句、真值表达式、条件表达式
- 选择语句
### day04
- for语句、continue、字符串
- 容器类通用操作
### day05
- 容器及相关方法、深拷贝与浅拷贝
- 列表 VS 字符串
### day06
- 列表推导式、元组、字典
### day07
- 集合、固定集合
- 双层for、列表推导式嵌套
- 函数
### day08
- 函数返回值
- 函数内存图
- 作用域
- 函数参数：形式参数、实际参数
### day09
- 类与对象
### day10
- 类、类成员、静态方法
### day11
- 封装、property
### day12
- ***
### day13
- 继承
### day14
- 内置可重写函数
- 运算符重载
- 多继承
- 模块
### day15
- 时间处理
- 包
- 自定义异常类
### day16
- 可迭代对象
- 迭代器
- 生成器
### day17
- 函数式编程
- lambda 匿名函数
### day18
- 内置高阶函数
- 外部嵌套作用域
- 闭包
### day19
- 装饰器

## 阶段二
### 2.1 

Linux:
- 在文件中进行查找: /xxx enter --> n-下一个 N-上一个
- 快速切换输入法: win+space

Django:
- 创建project: django-admin startproject project_name
- 启动项目: python3 manage.py runserver
- Django：Pycharm调试
    - Edit Configuration-->manager.py-->runserver
- 创建应用app:
    - 用manage.py中的子命令startapp创建应用文件夹
      - python3 manage.py startapp xxx
    - 在settings.py的INSTALLED_APPS列表中配置安装此应用
- 数据库迁移:
  - python3 manage.py makemigrations
  - python3 manage.py migrate

admin后台数据库管理:

`使用步骤:`
1. 创建后台管理帐号:
   - 后台管理--创建管理员帐号
   - kycheng    kycheng123456
     - `$ python3 manage.py createsuperuser`
     - 根据提示完成注册
2. 用注册的帐号登陆后台管理界面
    - 后台管理的登录地址:
        - <http://127.0.0.1:8000/admin>

### 项目开发
- 1 创建工程
- 2 配置mysql数据库
  - 1 创建数据库
    `create database xxx default charset utf8 collate utf8_general_ci`
  - 2 配置settings.py
  - 3 在__init__.py中添加
    `pymysql.install_as_MySQLdb()`
- 3 创建应用，编写模型类
  - python3 manage.py startapp xxx
  - 在settings.py中进行注册
  - 编写模型类
  - 数据库迁移
    - `python3 manage.py makemigrations`
    - `python3 manage.py migrate`
- 4 添加注册功能
  - 1 创建模板 `template/user/register.html`
  - 2 编写视图函数 `def reg_view(retuqest)`
  - 3 添加分布式路由 `/user/reg`

跨域相关：
  - sudo pip3 install django-cors-headers
  - pip3 freeze|grep 'cors'

linux:
  - 文件中搜索： `/xxx`
  - 文件中显示行数：`:set nu`
  - xxx