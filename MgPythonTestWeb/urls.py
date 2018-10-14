"""MgPythonTestWeb URL Configuration

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
from Test1 import views as Test1Views
from Test1.Controls import homeview as Test1ControlsViews

urlpatterns = [
    # url(r'^hello$', view1.hello),#1.8以前的版本格式,可兼容使用
    path('admin/', admin.site.urls),
    path('Test1Home/',Test1Views.home),
    path('Test1ControlsHome/',Test1ControlsViews.home),
]
