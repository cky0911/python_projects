# Generated by Django 4.2 on 2023-10-16 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0002_alter_userprofile_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='题目')),
                ('category', models.CharField(max_length=20, verbose_name='文章分类')),
                ('limit', models.CharField(max_length=10, verbose_name='文章权限')),
                ('introduce', models.CharField(max_length=90, verbose_name='文章简介')),
                ('content', models.TextField(verbose_name='文章内容')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.userprofile')),
            ],
            options={
                'db_table': 'topic',
            },
        ),
    ]
