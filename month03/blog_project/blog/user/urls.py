from django.urls import path, re_path
from . import views

urlpatterns = [
    # http://127.0.0.1:8000/v1/users
    path('', views.users),
    # http://127.0.0.1:8000/v1/users/<username>
    re_path(r'^/(?P<username>\w+)$', views.users),
    # http://127.0.0.1:8000/v1/users/<username>/avatar
    re_path(r'^/(?P<username>\w+)/avatar$', views.user_avatar),
]
