from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'movie/list.html')

def detail(request):
    return render(request,'movie/detail.html')

def search(request):
    return render(request,'movie/search.html')

