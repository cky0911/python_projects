import json

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def load_test(request):
    return render(request, 'load_test.html')


def load_test_server(request):
    return render(request, 'load_test_server.html')


def jquery_get(request):
    return render(request, 'jquery_get.html')


def jquery_get_server(request):
    d = {'uname': 'zhangsan', 'age': 18}
    return HttpResponse(json.dumps(d), content_type='application/json')


def jquery_post(request):
    return render(request, 'jquery_post.html')


def jquery_post_server(request):
    d = {'msg': 'post is ok!', 'code': 101}
    return HttpResponse(json.dumps(d), content_type='application/json')


def jquery_ajax(request):
    return render(request, 'jquery_ajax.html')


def jquery_ajax_server(request):
    d = {'msg': 'post is ok!', 'code': 201}
    return HttpResponse(json.dumps(d), content_type='application/json')


def jquery_ajax_user(request):
    return render(request, 'jquery_ajax_user.html')


def jquery_ajax_user_server(request):
    d = [{'name': 'lili', 'age': 21}, {'name': 'ljj', 'age': 25}]
    return HttpResponse(json.dumps(d), content_type='application/json')


def cross(request):
    return render(request, 'cross.html')


def cross_server(request):
    func = request.GET.get('callback')
    # func('str)
    return HttpResponse(func + "('cross success')")


def cross_server_json(request):
    func = request.GET.get('callback')
    d = {'msg': 'post is ok!', 'code': 301}
    return HttpResponse(func + "(" + json.dumps(d) + ")")
