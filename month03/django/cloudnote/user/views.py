from django.shortcuts import render
from . import models
from django.http import HttpResponse, HttpResponseRedirect
from . import forms


# Create your views here.
def reg_view(request):
    if request.method == 'GET':
        return render(request, 'user/register.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password_1 = request.POST.get('password_1')
        password_2 = request.POST.get('password_2')
        # 验证数据的合法性
        if len(username) < 2:
            username_error = "当前用户名长度过短"
            return render(request, 'user/register.html', locals())
        # 密码验证： password_1不能为空 password_1与password_2一致 数据库中是否已经存在当前注册的username
        password_1 = request.POST.get('password_1')
        password_2 = request.POST.get('password_2')
        if not password_1 or not password_2:
            password_1_error = '密码不能为空'
            return render(request, 'user/register.html', locals())

        if password_1 != password_2:
            password_2_error = '两次输入的密码不一致'
            return render(request, 'user/register.html', locals())

        # 查询用户是否存在
        try:
            old_user = models.User.objects.get(username=username)
            # 当前用户名已被注册
            username_error = '当前用户名已存在'
            return render(request, 'user/register.html')
        except Exception as e:
            print('---%s get error is %s' % (username, e))
            # 没有查到的情况下 报错，证明当前用户名为可用状态
            user = models.User.objects.create(username=username, password=password_1)
            html = "注册成功 点击<a href='/user/login'>进入登录页面</a>"

            # resp = HttpResponse(html)
            # resp.set_cookie("username", username)
            # return resp

            # 存session
            # request.session['username'] = username
            return HttpResponse(html)


def login_view(request):
    if request.method == 'GET':
        username = request.COOKIES.get('username', '')
        return render(request, 'user/login.html', locals())

    elif request.method == 'POST':
        # 处理登录逻辑
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == '':
            username_error = '用户名不能为空'
            return render(request, 'user/login.html', locals())
        try:
            user = models.User.objects.get(username=username, password=password)
            request.session['user'] = {
                'username': username,
                'id': user.id
            }
            resp = HttpResponseRedirect('/note')
            # if 'remember' in request.POST:
            #     resp.set_cookie('username', username)
            return resp
        except:
            password_error = "用户名或密码不正确"
            return render(request, 'user/login.html', locals())


def logout_view(request):
    # 删除session
    if 'user' in request.session:
        del request.session['user']
    resp = HttpResponseRedirect('/note')
    # 删除cookie
    if 'username' in request.COOKIES:
        resp.delete_cookie('username')
    return resp


def reg2_view(request):
    if request.method == 'GET':
        myform = forms.MyRegForm()
        return render(request, 'user/register2.html', locals())
    elif request.method == 'POST':
        myform = forms.MyRegForm(request.POST)
        if myform.is_valid():
            dict = myform.cleaned_data
            username = dict['username']
            password1 = dict['password1']
            password2 = dict['password2']
            return HttpResponse(str(dict))
        else:
            return HttpResponse("表单验证失败")