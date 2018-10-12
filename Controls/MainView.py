from django.http import HttpResponse
from django.shortcuts import render

def showMainView(request):
    context={}
    context["title"]="测试主页面"
    context["hello"]="This is MainView"
    return render(request,"MainView.html",context)