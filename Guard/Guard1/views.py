from django.shortcuts import render
from django.http import HttpResponse
# Create your views here

def index(request):
    return render(request,'guard1/index.html')

def index1(request):
    return render(request,'guard1/arsen.html')

def index2(request):
    return render(request,'guard1/index.html')

def index3(request):
    return render(request,'guard1/login.html')

def index4(request):
    return render(request,'guard1/Security_Issue.html')