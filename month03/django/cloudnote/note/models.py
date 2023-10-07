from django.db import models

from user.models import User


# Create your models here.
class Note(models.Model):
    objects = models.Manager()
    title = models.CharField('标题', max_length=100)
    content = models.TextField('内容')
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    mod_time = models.DateTimeField('修改时间', auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
