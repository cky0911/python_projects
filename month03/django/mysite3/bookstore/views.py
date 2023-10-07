from django.shortcuts import render
from django.http import HttpResponse
from . import models


# Create your views here.
def add_view(request):
    try:
        # 方法1
        # abook = models.Book.objects.create(title='Python从入门到精通', price=68, desc='入门推荐书籍')
        # return HttpResponse("add book successfully.")
        # 方法2
        abook = models.Book(title='Java从入门到精通', price=78, desc='入门推荐书籍')
        # 执行sql
        abook.save()
        return HttpResponse("add book successfully.")
    except Exception as e:
        return HttpResponse("add book failure.")
