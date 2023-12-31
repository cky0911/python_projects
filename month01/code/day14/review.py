"""
    复习
        面向对象：考虑问题从对象的角度出发.
        抽象：从多个事物中，舍弃个别的/非本质的特征(不重要)，
             抽出共性的本质(重要的)过程。
        三大特征：
            封装：将每个变化点单独分解到不同的类中。
                例如：老张开车去东北
                做法：定义人类，定义车类。

            继承：重用现有类的功能和概念，并在此基础上进行扩展。
                   统一概念
                例如：图形管理器，统计圆形/矩形.....面积。
                做法：用图形类代表/约束，圆形/矩形..具有计算面积的方法.

            多态：调用父"抽象的"方法，执行子类"具体的"方法.
                重写：覆盖父类那个比较抽象的方法。
                例如：图形管理器调用图形的计算面积方法
                     具体图形必须重写图形的计算面积方法。
                继承是共性(计算面积)，多态个性(长*宽 / pi *r**2)。

        设计原则
            开闭原则：允许增加新功能，不允许修改客户端代码.
            单一职责：一个类有且只有一个改变的原因.
            依赖倒置：调用抽象(父)，不要调用具体(子);
                    抽象不要依赖具体.
            组合复用：如果仅仅是代码的复用，优先使用组合.

        类与类关系
            泛化[继承](做成爸爸)
            关联(做成成员变量)
            依赖(做成方法参数)
"""
