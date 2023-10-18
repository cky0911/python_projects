import json

from django.http import JsonResponse
from django.shortcuts import render

from message.models import Message
from tools.login_check import logging_check
from topic.models import Topic


# Create your views here.
@logging_check('POST')
def messages(request, topic_id):
    if request.method != 'POST':
        result = {'code': 50001, 'error': 'request method error!'}
        return JsonResponse(result)
    # 发表留言/回复
    user = request.user
    json_str = request.body
    json_obj = json.loads(json_str)
    content = json_obj.get('content')
    if not content:
        result = {'code': 50002, 'error': 'empty content!'}
        return JsonResponse(result)
    parent_id = json_obj.get('parent_id', 0)

    try:
        topic = Topic.objects.get(id=topic_id)
    except:
        result = {'code': 50003, 'error': 'topic not found!'}
        return JsonResponse(result)
    # 私有博客只能博主留言
    if topic.limit == 'private':
        # 检查身份
        if user.username != topic.author.username:
            result = {'code': 50004, 'error': 'No comment permission!'}
            return JsonResponse(result)
    # 创建数据
    Message.objects.create(content=content, publisher=user, topic=topic, parent_message=parent_id)
    return JsonResponse({'code': 200, 'data': {}})
