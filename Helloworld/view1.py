from django.http import HttpResponse
from django.shortcuts import render

def hello(result):
    return HttpResponse("Hello World！")
def showView1(request):
    context={}
    context["hello"]="This is Change Value"
    return render(request,"view1.html",context)