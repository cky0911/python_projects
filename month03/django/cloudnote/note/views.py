import os

from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from user.models import User
from .models import Note
from django.core.paginator import Paginator


# Create your views here.

def index_view(request):
    return render(request, 'note/index.html', locals())


def check_login(fun):
    def wrap(request, *args, **kwargs):
        if not hasattr(request, 'session'):
            return HttpResponseRedirect('/user/login')
        if 'user' not in request.session:
            return HttpResponseRedirect('/user/login')
        return fun(request, *args, **kwargs)

    return wrap


@check_login
def list_view(request):
    user_id = request.session['user']['id']
    # 根据已登录的用户id找到当前登录的用户
    user = User.objects.get(id=user_id)
    notes = user.note_set.all()
    return render(request, 'note/note_list.html', locals())


@check_login
def add_view(request):
    if request.method == 'GET':
        return render(request, 'note/add_note.html')
    elif request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        # 存数据
        user_id = request.session['user']['id']
        user = User.objects.get(id=user_id)
        note = Note(user=user)
        note.title = title
        note.content = content
        note.save()
        return HttpResponseRedirect('/note/note_list')


def mod_view(request, id):
    # 得到当前登录用户的模型对象
    user_id = request.session['user']['id']
    user = User.objects.get(id=user_id)
    note = Note.objects.get(user=user, id=id)
    if request.method == 'GET':
        return render(request, 'note/mod_note.html', locals())
    elif request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        note.title = title
        note.content = content
        note.save()
        return HttpResponseRedirect('/note/note_list')


def del_view(request, id):
    user_id = request.session['user']['id']
    user = User.objects.get(id=user_id)
    note = Note.objects.get(user=user, id=id)
    note.delete()

    return HttpResponseRedirect('/note/note_list')


@check_login
def pagination_view(request):
    # 查数据
    user_id = request.session['user']['id']
    # 根据已登录的用户id找到当前登录的用户
    user = User.objects.get(id=user_id)
    notes = user.note_set.all()
    # 在此处添加分页功能
    paginator = Paginator(notes, 5)
    # 得到当前的页码数
    cur_page = request.GET.get('page', 1)
    cur_page = int(cur_page)
    page = paginator.page(cur_page)
    return render(request, 'note/note_list.html', locals())


def upload_view(request):
    if request.method == 'GET':
        return render(request, 'note/upload.html')
    elif request.method == 'POST':
        a_file = request.FILES['file_img']
        print("上传文件名是:", a_file.name)
        # 计算保存文件的位置
        filename = os.path.join(settings.MEDIA_ROOT, a_file.name)
        with open(filename, 'wb') as fw:
            data = a_file.file.read()
            fw.write(data)
            return HttpResponse("接收文件:" + a_file.name + "成功")
    raise Http404
