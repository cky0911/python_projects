from django.urls import path, re_path
from . import views

urlpatterns = [
    # 这里用path失败了
    re_path(r'^reg$', views.reg_view),
    re_path(r'^reg2', views.reg2_view),
    path('login', views.login_view),
    path('logout', views.logout_view),
]
