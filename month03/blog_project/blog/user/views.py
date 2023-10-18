import hashlib
import json

from django.http import JsonResponse
from django.shortcuts import render

from btoken.views import make_token
from user.models import UserProfile
from tools.login_check import logging_check


@logging_check('PUT')
# Create your views here.
def users(request, username=None):
    # http://127.0.0.1:8000/v1/users GET
    if request.method == 'GET':
        if username:
            try:
                user = UserProfile.objects.get(username=username)
            except Exception as e:
                user = None
            if not user:
                result = {'code': 10108, 'error': 'User is not existed !'}
                return JsonResponse(result)
            # 判断是否有查询字符串
            if request.GET.keys():
                # 有查询字符串
                data = {}
                for k in request.GET.keys():
                    # 判断查询字符串的key 是否在表里有该对应的字段
                    if hasattr(user, k):
                        v = getattr(user, k)
                        if k == 'avatar':
                            data[k] = str(v)
                        else:
                            data[k] = v
                result = {'code': 200, 'username': username, 'data': data}
                return JsonResponse(result)
            else:
                # 无查询字符串  全量查询
                result = {'code': 200, 'username': username,
                          'data': {'nickname': user.nickname, 'email': user.email, 'sign': user.sign, 'info': user.info,
                                   'avatar': str(user.avatar)}}
                return JsonResponse(result)
        else:
            print('---全量---')
            all_user = UserProfile.objects.all()
            all_data = []
            for u in all_user:
                d = {'nickname': u.nickname, 'email': u.email, 'sign': u.sign}
                all_data.append(d)
            return JsonResponse({'code': 200, 'data': all_data})
    elif request.method == 'POST':
        json_str = request.body
        if not json_str:
            result = {'code': 10100, 'error': 'Please give me data'}
            return JsonResponse(result)
        json_obj = json.loads(json_str)
        username = json_obj.get('username')
        email = json_obj.get('email')
        password_1 = json_obj.get('password_1')
        password_2 = json_obj.get('password_2')
        if not username:
            result = {'code': 10101, 'error': 'Please give me username'}
            return JsonResponse(result)
        if not email:
            result = {'code': 10102, 'error': 'Please give me email'}
            return JsonResponse(result)

        if not password_1 or not password_2:
            result = {'code': 10103, 'error': 'Please give me password'}
            return JsonResponse(result)

        if password_1 != password_2:
            result = {'code': 10104, 'error': 'The password is not same!'}
            return JsonResponse(result)
        # 检查当前用户名是否可用
        old_user = UserProfile.objects.filter(username=username)
        if old_user:
            result = {'code': 10105, 'error': 'The username is already existed!'}
            return JsonResponse(result)
        # 密码进行哈希－md5
        p_m = hashlib.md5()
        p_m.update(password_1.encode())
        sign = info = ''
        # 创建用户
        try:
            UserProfile.objects.create(username=username, password=p_m.hexdigest(), nickname=username, email=email,
                                       sign=sign, info=info)
        # 数据库挂了或者用户名已经存在
        except Exception as e:
            print(e)
            result = {'code': 10106, 'error': 'The username is already used!'}
            return JsonResponse(result)

        # 生成token
        token = make_token(username)
        result = {'code': 200, 'username': username, 'data': {'token': token}}
        return JsonResponse(result)
    elif request.method == 'PUT':
        user = request.user
        json_str = request.body
        if not json_str:
            result = {'code': 10109, 'error': 'Please give me data'}
            return JsonResponse(result)

        json_obj = json.loads(json_str)

        if 'sign' not in json_obj:
            result = {'code': 10110, 'error': 'Please give me sign !'}
            return JsonResponse(result)

        if 'info' not in json_obj:
            result = {'code': 10111, 'error': 'Please give me info'}
            return JsonResponse(result)

        # if 'nickname' not in json_obj:
        #     result = {'code': 10112, 'error': 'Please give me nickname'}
        #     return JsonResponse(result)

        # nickname = json_obj['nickname']
        request.user.sign = json_obj.get('sign')
        request.user.info = json_obj.get('info')
        request.user.save()
        result = {'code': 200, 'username': request.user.username}
        return JsonResponse(result)
    else:
        raise
    # return JsonResponse({'code': 200})


@logging_check('POST')
def user_avatar(request, username):
    # # 用户上传头像
    if request.method != 'POST':
        result = {'code': 10114, 'error': 'Please use POST'}
        return JsonResponse(result)

    user = request.user

    # 前端 username 后端 request.user.username
    if username != request.user.username:
        result = {'code': 10117, 'error': 'Request error!'}
        return JsonResponse(result)

    avatar = request.FILES['avatar']
    if not avatar:
        result = {'code': 10116, 'error': 'No avatar'}
        return JsonResponse(result)
    user.avatar = avatar
    user.save()
    result = {'code': 200, 'username': username}
    return JsonResponse(result)
