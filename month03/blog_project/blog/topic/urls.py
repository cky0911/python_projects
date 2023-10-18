from django.urls import path, re_path
from . import views

urlpatterns = [
    # http://127.0.0.1:8000/v1/topics/<author>
    re_path(r'^/(?P<author_id>\w+)$', views.topics),

]
