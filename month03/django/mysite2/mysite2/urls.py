"""
URL configuration for mysite2 project.

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
    path('test_get', views.test_get),
    path('test_get_form', views.test_get),
    path('sum', views.sum_view),
    path('test_post', views.test_post),
    path('test_post_form', views.test_post),
    path('test_login_html', views.test_login_html),
    path('test_html', views.test_html),
    path('test_if', views.test_if),
    path('calculate', views.calculate_exercise),
    path('test_for', views.test_for),

    path('test_base', views.test_base),
    path('test_music', views.test_music),
    path('test_sport', views.test_sport),
]
