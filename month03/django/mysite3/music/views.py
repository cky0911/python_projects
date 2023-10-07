from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def page1_view(request):
    return HttpResponse('我是music_app下的主页1')


def page2_view(request):
    return HttpResponse('我是music_app下的主页2')


def page3_view(request):
    return HttpResponse('我是music_app下的主页3')
