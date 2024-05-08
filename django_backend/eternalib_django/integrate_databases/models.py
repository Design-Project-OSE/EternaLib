from django.db import models

class Movies(models.Model):
    name=models.CharField(max_length=100,name="İsim")
    production=models.CharField(max_length=100,name="Yapımcı")
    about=models.TextField(name="Hakkında")
    genres=models.TextField(name="Tür")
    release=models.DateTimeField(name="Çıkış Tarihi")
    imdb=models.IntegerField(name="IMDB")
    metascritic=models.IntegerField(name="Metacritic")
    background=models.CharField(max_length=500,name="Arkaplan")
    poster=models.CharField(max_length=500,name="Poster")
    trailer=models.CharField(max_length=500,name="Trailer")
    savedate=models.DateTimeField(auto_now_add= True)
    
class Games(models.Model):
    name=models.CharField(max_length=100,name="İsim")
    production=models.CharField(max_length=100,name="Yapımcı")
    about=models.TextField(name="Hakkında")
    genres=models.TextField(name="Tür")
    release=models.DateTimeField(name="Çıkış Tarihi")
    imdb=models.IntegerField(name="IMDB")
    metascritic=models.IntegerField(name="Metacritic")
    background=models.CharField(max_length=500,name="Arkaplan")
    poster=models.CharField(max_length=500,name="Poster")
    trailer=models.CharField(max_length=500,name="Trailer")
    savedate=models.DateTimeField(auto_now_add= True)
    
class Books(models.Model):
    name=models.CharField(max_length=100,name="İsim")
    production=models.CharField(max_length=100,name="Yapımcı")
    about=models.TextField(name="Hakkında")
    genres=models.TextField(name="Tür")
    release=models.DateTimeField(name="Çıkış Tarihi")
    background=models.CharField(max_length=500,name="Arkaplan")
    poster=models.CharField(max_length=500,name="Poster")
    savedate=models.DateTimeField(auto_now_add= True)
