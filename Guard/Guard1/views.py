from django.shortcuts import render
from django.http import HttpResponse
# Create your views here

def index(request):
    return render(request,'guard1/index.html'),

def index1(request):
    return render(request,'Guard1/index.html'),