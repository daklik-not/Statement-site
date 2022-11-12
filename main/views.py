from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse



def hello_there(request):
    zero=0
    return render(request,'main/home.html',{"zero":zero})
