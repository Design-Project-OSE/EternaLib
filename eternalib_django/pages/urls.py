from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name='Homepage'),
    path('login',views.pages_login,name='Login'),
    path('signup',views.pages_signup,name='SignUp'),
    path('movies',views.pages_movies,name='Movies'),
    path('books',views.pages_book,name='Books'),
    path('games',views.pages_game,name='Games'),
]