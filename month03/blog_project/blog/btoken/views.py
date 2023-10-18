import hashlib
import json
import time

import jwt
from django.http import JsonResponse
from django.shortcuts import render
from user.models import UserProfile


# Create your views here.
def tokens(request):
    # 即登录
    if request.method != 'POST':
        result = {'code': 10200, 'error': 'Please us post'}
        return JsonResponse(result)

    # 获取前端body中的数据 生成token
    json_str = request.body
    if not json_str:
        result = {'code': 10201, 'error': 'Please give me data'}
        return JsonResponse(result)
    json_obj = json.loads(json_str)

    username = json_obj.get('username')
    password = json_obj.get('password')
    if not username:
        result = {'code': 10202, 'error': 'Give me username !!!'}
        return JsonResponse(result)
    if not password:
        result = {'code': 10203, 'error': 'Give me password !!!'}
        return JsonResponse(result)

    user = UserProfile.objects.filter(username=username)
    if not user:
        result = {'code': 10204, 'error': 'Username or password is wrong !'}
        return JsonResponse(result)
    # filter得到的是集合
    user = user[0]
    # 对比密码
    p_m = hashlib.md5()
    p_m.update(password.encode())
    if p_m.hexdigest() != user.password:
        result = {'code': 10205, 'error': 'Username or password is wrong !!'}
        return JsonResponse(result)
    # 生成token
    token = make_token(username)
    result = {'code': 200, 'username': username, 'data': {'token': token}}
    return JsonResponse(result)


def make_token(username, expire=3600 * 24):
    key = '123456'
    now = time.time()
    payload = {'username': username, 'exp': now + expire}
    return jwt.encode(payload, key, algorithm='HS256')
