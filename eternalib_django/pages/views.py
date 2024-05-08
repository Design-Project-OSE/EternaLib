from django.shortcuts import render


def homepage(request):
    return render(request,'pages/homepage.html')

def pages_movies(request):
    return render(request,'pages/movies.html')

def pages_book(request):
    return render(request,'pages/book.html')

def pages_game(request):
    return render(request,'pages/games.html')

def pages_login(request):
    return render(request,'pages/login.html')

def pages_signup(request):
    return render(request,'pages/signup.html')