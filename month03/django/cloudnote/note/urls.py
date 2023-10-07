from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index_view),
    # path('note_list', views.list_view),
    path('note_list', views.pagination_view),
    path('add', views.add_view),
    re_path(r'mod/(\d+)', views.mod_view),
    re_path(r'del/(\d+)', views.del_view),
    path('upload', views.upload_view),
]
