import html
import json

from django.http import JsonResponse

from message.models import Message
from tools.login_check import logging_check, get_user_by_request
from .models import *


# Create your views here.
@logging_check('POST', 'DELETE')
def topics(request, author_id):
    if request.method == 'GET':
        # http://127.0.0.1:5000/<username>/topics
        # author_id 是被访问的博主的用户名
        authors = UserProfile.objects.filter(username=author_id)
        # authors有返回，author必然是authors第一个元素，因为username在表中为主键【唯一】
        if not authors:
            result = {'code': 10304, 'error': 'no author'}
            return JsonResponse(result)
        # 当前被访问博客的博主
        author = authors[0]
        # 获取当前访问者
        visitor = get_user_by_request(request)
        visitor_name = None
        if visitor:
            visitor_name = visitor.username
        t_id = request.GET.get('t_id')
        if t_id:
            # 查询用户具体博客内容
            t_id = int(t_id)
            is_self = False
            if visitor_name == author_id:
                is_self = True
                # 博主访问自己的博客
                try:
                    author_topic = Topic.objects.get(id=t_id)
                except Exception as e:
                    result = {'code': 10308, 'error': 'No topic'}
                    return JsonResponse(result)
            else:
                # 访客访问当前博客
                try:
                    author_topic = Topic.objects.get(id=t_id, limit='public')
                except Exception as e:
                    print('topic error')
                    print(e)
                    result = {'code': 10309, 'error': 'No topic'}
                    return JsonResponse(result)

            res = make_topic_res(author, author_topic, is_self)
            return JsonResponse(res)
        else:
            category = request.GET.get('category')
            if category in ['tec', 'no-tec']:
                # /v1/topics/<author_id>?category=[tec/no-tec] 用户全量数据
                if author_id == visitor_name:
                    # 博主访问自己的博客
                    topics = Topic.objects.filter(author_id=author_id, category=category)
                else:
                    # 访客
                    topics = Topic.objects.filter(author_id=author_id, category=category, limit='public')
            else:
                # /v1/topics/<author_id> 用户全量数据
                if author_id == visitor_name:
                    # 博主访问自己的博客 获取全部博客数据
                    topics = Topic.objects.filter(author_id=author_id)
                else:
                    # 访客 非博主本人 只获取public数据
                    topics = Topic.objects.filter(author_id=author_id, limit='public')
            res = make_topics_res(author, topics)
            return JsonResponse(res)
    elif request.method == 'POST':
        # TODO 校验request.user.username == author_id
        json_str = request.body
        if not json_str:
            result = {'code': 10300, 'error': 'Please give me data'}
            return JsonResponse(result)
        json_obj = json.loads(json_str)
        title = json_obj.get('title')
        # xss注入
        title = html.escape(title)
        if not title:
            result = {'code': 10301, 'error': 'Please give me title'}
            return JsonResponse(result)
        # 带有html标签样式的博客内容
        content = json_obj.get('content')
        # 纯文本的博客内容
        content_text = json_obj.get('content_text')
        if not content or not content_text:
            result = {'code': 10302, 'error': 'Please give me content !'}
            return JsonResponse(result)
        # 生成简介部分
        introduce = content_text[:30]
        limit = json_obj.get('limit')
        # 校验limit
        if limit not in ('public', 'private'):
            result = {'code': 10303, 'error': 'Your limit is not ok!'}
            return JsonResponse(result)
        category = json_obj.get('category')
        # 校验category
        if category not in ('tec', 'no-tec'):
            result = {'code': 10304, 'error': 'Your category is not ok!'}
            return JsonResponse(result)

        Topic.objects.create(title=title, category=category, limit=limit, introduce=introduce, content=content,
                             author=request.user)

        result = {'code': 200, 'username': request.user.username}
        return JsonResponse(result)
    elif request.method == 'DELETE':
        # 删除一定要校验token中的username和视图函数传进来的author_id
        if author_id != request.user.username:
            result = {'code': 10305, 'error': 'The author id is error'}
            return JsonResponse(result)
        topic_id = request.GET.get('topic_id')
        if not topic_id:
            result = {'code': 10306, 'error': 'No topic id'}
            return JsonResponse(result)
        # 查询指定文章
        topic_id = int(topic_id)
        try:
            topic = Topic.objects.get(id=topic_id)
        except Exception as e:
            result = {'code': 10307, 'error': 'No topic'}
            return JsonResponse(result)
        topic.delete()
        return JsonResponse({'code': 200})

    return JsonResponse({'code': 200000})


def make_topics_res(author, topics):
    res = {'code': 200, 'data': {}}
    topics_res = []
    for topic in topics:
        d = {}
        d['id'] = topic.id
        d['title'] = topic.title
        d['category'] = topic.category
        d['introduce'] = topic.introduce
        d['author'] = author.nickname
        d['created_time'] = topic.created_time.strftime('%Y-%m-%d %H:%M:%S')
        # TODO content?
        topics_res.append(d)

    res['data']['nickname'] = author.nickname
    res['data']['topics'] = topics_res
    # {'code':200, 'data':{'nickname':xxx,'topics':[{xxx},{xx}]}}
    return res


def make_topic_res(author, author_topic, is_self):
    """
    拼接详情页返回的数据
    :param author:
    :param author_topic:
    :param is_self:
    :return:
    """
    if is_self:
        # 博主访问自己 上一篇 下一篇
        next_topic = Topic.objects.filter(id__gt=author_topic.id, author=author).first()
        last_topic = Topic.objects.filter(id__lt=author_topic.id, author=author).last()
    else:
        # 游客访问当前博客
        next_topic = Topic.objects.filter(id__gt=author_topic.id, author=author, limit='public').first()
        last_topic = Topic.objects.filter(id__lt=author_topic.id, author=author, limit='public').last()

    if next_topic:
        next_id = next_topic.id
        next_title = next_topic.title
    else:
        next_id = None
        next_title = None

    if last_topic:
        last_id = last_topic.id
        last_title = last_topic.title
    else:
        last_id = None
        last_title = None

    result = {'code': 200, 'data': {}}
    result['data']['nickname'] = author.nickname
    result['data']['title'] = author_topic.title
    result['data']['category'] = author_topic.category
    result['data']['introduce'] = author_topic.introduce
    result['data']['content'] = author_topic.content
    result['data']['created_time'] = author_topic.created_time.strftime('%Y-%m-%d %H:%M:%S')
    result['data']['next_id'] = next_id
    result['data']['next_title'] = next_title
    result['data']['last_id'] = last_id
    result['data']['last_title'] = last_title
    result['data']['author'] = author.nickname

    # 拼message返回
    all_messages = Message.objects.filter(topic=author_topic).order_by('-created_time')
    # 存储所有的留言
    msg_list = []
    # 存储 {'parent_message':[回复..回复..]}
    reply_dict = {}
    msg_count = 0
    for msg in all_messages:
        msg_count += 1
        if msg.parent_message:
            # 回复
            if msg.parent_message not in reply_dict:
                reply_dict[msg.parent_message] = []
                reply_dict[msg.parent_message].append(
                    {'msg_id': msg.id, 'content': msg.content, 'publisher': msg.publisher.nickname,
                     'publisher_avatar': str(msg.publisher.avatar),
                     'created_time': msg.created_time.strftime('%Y-%m-%d %H:%M:%S')})
            else:
                reply_dict[msg.parent_message].append(
                    {'msg_id': msg.id, 'content': msg.content, 'publisher': msg.publisher.nickname,
                     'publisher_avatar': str(msg.publisher.avatr),
                     'created_time': msg.created_time.strftime('%Y-%m-%d %H:%M:%S')})
        else:
            # 留言
            msg_list.append({'id': msg.id, 'content': msg.content, 'publisher': msg.publisher.nickname,
                             'publisher_avatar': str(msg.publisher.avatar),
                             'created_time': msg.created_time.strftime('%Y-%m-%d %H:%M:%S'), 'reply': []})

    # 合并
    for m in msg_list:
        if m['id'] in reply_dict:
            m['replay'] = reply_dict[m['id']]

    result['data']['messages'] = msg_list
    result['data']['messages_count'] = msg_count
    return result
