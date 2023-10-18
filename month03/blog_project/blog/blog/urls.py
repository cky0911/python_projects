"""
URL configuration for blog project.

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', views.test_api),
    # http://127.0.0.1:8000/v1/users
    path('v1/users', include('user.urls')),
    path('v1/tokens', include('btoken.urls')),
    path('v1/topics', include('topic.urls')),
    path('v1/messages', include('message.urls')),
]

# 生成媒体资源路由 ->上传数据 -> document_root 去找文件
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
