import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.core import serializers

from .models import User


# Create your views here.

def xhr(request):
    return render(request, 'xhr.html')


def get_xhr(request):
    return render(request, 'get_xhr.html')


def get_xhr_server(request):
    if request.GET.get('uname'):
        uname = request.GET['uname']
        return HttpResponse('Welcome %s' % uname)
    return HttpResponse('ajax response')


def register_view(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        uname = request.POST.get('uname')
        if not uname:
            return HttpResponse('please input username!')
        pwd = request.POST.get('pwd')
        if not pwd:
            return HttpResponse('please input password!')
        nickname = request.POST.get('nickname')
        if not nickname:
            return HttpResponse('please input nickname!')
        try:
            User.objects.create(uname=uname, pwd=pwd, nickname=nickname)
        except Exception as e:
            return HttpResponse('register failed! retry later...')

        return HttpResponse('register success!')


def check_uname_view(request):
    # 获取ajax传过来的用户名
    uname = request.GET.get('uname')
    # 校验用户
    user = User.objects.filter(uname=uname)
    if user:
        return HttpResponse('1')
    return HttpResponse('0')


def make_post(request):
    if request.method == 'GET':
        return render(request, 'make_post.html')
    elif request.method == 'POST':
        # 获取表单数据
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        return HttpResponse('post is ok! %s %s' % (uname, pwd))
    else:
        raise


def get_user(request):
    return render(request, 'get_user.html')


def get_user_server(request):
    users = User.objects.all()
    msg = ''
    for u in users:
        msg += '%s_%s_%s|' % (u.uname, u.pwd, u.nickname)
    last_msg = msg[0:-1]
    return HttpResponse(last_msg)


def json_obj(request):
    return render(request, 'json_obj.html')


def json_dumps(request):
    # 1 json序列化  python-obj -> json串
    # 2 json反序列化 json串 -> Python-obj

    # 序列化单个对象
    # dic = {
    #     'name': 'wanglaoshi',
    #     'age': 18
    # }
    # json_str = json.dumps(dic, sort_keys=True, separators=(',', ':'))
    # return HttpResponse(json_str)

    # 序列化多个对象
    # s = [
    #     {
    #         'name': 'guo',
    #         'age': 18
    #     },
    #     {
    #         'name': 'wang',
    #         'age': 19
    #     }
    # ]
    # json_str = json.dumps(s, sort_keys=True, separators=(',', ':'))
    # return HttpResponse(json_str, content_type='application/json')

    # version1.0
    # all_users = User.objects.all()
    # json_str_all = serializers.serialize('json', all_users)
    # return HttpResponse(json_str_all, content_type='application/json')

    # version2.0
    d = []
    all_users = User.objects.all()
    for u in all_users:
        d.append({'name': u.uname})
    return JsonResponse({'all_user': d})
    # return HttpResponse(json.dumps(d), content_type='application/json')
