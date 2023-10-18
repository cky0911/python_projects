# Generated by Django 4.2 on 2023-10-14 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('username', models.CharField(max_length=11, primary_key=True, serialize=False, verbose_name='用户名')),
                ('nickname', models.CharField(max_length=30, verbose_name='昵称')),
                ('email', models.EmailField(max_length=50, verbose_name='电子邮箱')),
                ('password', models.CharField(max_length=32, verbose_name='密码')),
                ('sign', models.CharField(max_length=50, verbose_name='个性签名')),
                ('info', models.CharField(default='', max_length=150, verbose_name='个人描述')),
                ('avatar', models.ImageField(upload_to='avatar/')),
            ],
            options={
                'db_table': 'user_profile',
            },
        ),
    ]
