from django.urls import path, re_path
from . import views

urlpatterns = [
    # http://127.0.0.1:8000/v1/messages/<topic_id>
    re_path(r'^/(?P<topic_id>\d+)$', views.messages),

]