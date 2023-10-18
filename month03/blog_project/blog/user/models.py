from django.db import models


# Create your models here.

# class_name: UserProfile
# db_table_name: user_profile
class UserProfile(models.Model):
    objects = models.Manager()
    username = models.CharField(max_length=11, verbose_name='用户名', primary_key=True)
    nickname = models.CharField(max_length=30, verbose_name='昵称')
    email = models.EmailField(max_length=50, null=True, verbose_name='电子邮箱')
    password = models.CharField(max_length=32, verbose_name='密码')
    sign = models.CharField(max_length=50, verbose_name='个性签名')
    info = models.CharField(max_length=150, default='', verbose_name='个人描述')
    # created_time = models.DateTimeField(auto_now_add=True)
    # updated_time = models.DateTimeField(auto_now=True)
    avatar = models.ImageField(upload_to='avatar/')

    class Meta:
        db_table = 'user_profile'
