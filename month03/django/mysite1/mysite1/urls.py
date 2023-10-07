"""
URL configuration for mysite1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('page/', views.page_view),
    path('', views.index_view),
    path('page1/', views.page1_view),
    path('page2/', views.page2_view),
    re_path(r'^page(\d+)', views.pagen_view),
    re_path(r'^(\d+)/(\w{3})/(\d+)', views.math_view),
    re_path(r'^person/(?P<name>\w+)/(?P<age>\d{1,2})', views.person_view),

    # 127.0.0.1:8000/birthday/year/month/day
    re_path(r'^birthday/(?P<y>\d{4})/(?P<m>\d{1,2})/(?P<d>\d{1,2})', views.birthday_view),
    # 127.0.0.1:8000/birthday/month/day/year
    re_path(r'^birthday/(?P<m>\d{1,2})/(?P<d>\d{1,2})/(?P<y>\d{4})', views.birthday_view),

    re_path(r'^mypage', views.mypage_view),
]
