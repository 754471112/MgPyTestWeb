"""Helloworld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from . import view1
from django.conf.urls import url
from Controls import MainView

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
urlpatterns = [
    #url方法有四个参数:regex正则表达式,view用于执行与正则表达式匹配的 URL 请求
    #kwargs:视图使用的字典类型的参数(可选)、name:用来反向获取URL(可选)
    url(r'^hello$', view1.hello),
    url(r"^showView1",view1.showView1),
    url(r"mainview",MainView.showMainView),
]
