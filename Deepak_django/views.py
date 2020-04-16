from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    params={'name':request.GET.get('name',''),'gender':int(request.GET.get('gender','-1'))}
    return render(request,'index.html',params)

def about(request):
    return HttpResponse("<h1> About us </h1>")