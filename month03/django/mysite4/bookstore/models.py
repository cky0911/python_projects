from django.db import models


# Create your models here.
class Book(models.Model):
    objects = models.Manager()
    # 书名 非空 唯一
    title = models.CharField(max_length=30, unique=True, verbose_name='书名')
    # 出版社
    pub = models.CharField(max_length=50, null=True, verbose_name='出版社')
    # 定价 00000.00
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0.0, verbose_name='定价')
    # 零售价
    market_price = models.DecimalField(max_digits=7, decimal_places=2, default=99999, verbose_name='零售价')

    def __str__(self):
        return "书名: %s, 出版社: %s, 定价: %s" % (self.title, self.pub, self.price)


class Author(models.Model):
    # 姓名 非空
    name = models.CharField(max_length=30)
    # 年龄 非空 缺省值1
    age = models.IntegerField(verbose_name='年龄', default=1)
    # 邮箱 允许为空
    email = models.EmailField(verbose_name='邮箱', null=True)

    def __str__(self):
        return "作者：" + str(self.name)
