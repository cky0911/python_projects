from django.urls import path, include
from . import views

urlpatterns = [
    path('xhr', views.xhr, name='xhr'),
    path('get-xhr', views.get_xhr, name='get_xhr'),
    path('get-xhr-server', views.get_xhr_server, name='get_xhr_server'),
    path('register', views.register_view, name='register'),
    path('check-uname', views.check_uname_view, name='check_uname'),
    path('make-post', views.make_post, name='make_post'),
    path('get-user', views.get_user, name='get_user'),
    path('get-user-server', views.get_user_server, name='get_user_server'),
    path('json-obj', views.json_obj, name='json_obj'),
    path('json-dumps', views.json_dumps, name='json_dumps'),
]
