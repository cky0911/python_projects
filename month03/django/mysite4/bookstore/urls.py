from django.contrib import admin
from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('add', views.add_view),
    path('get_all', views.show_all_books),
    re_path(r'update_book/(\d+)', views.update_book_view),
    re_path(r'delete_book/(\d+)', views.delete_book_view),
    path('set_cookie', views.set_cookies_view),
    path('get_cookie', views.get_cookies_view),
]
