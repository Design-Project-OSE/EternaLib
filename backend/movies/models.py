from django.db import models

class category_movie(models.Model):
    name=models.CharField(max_length=25,verbose_name="Tür İsmi")
    category_id=models.CharField(max_length=2,verbose_name="Tür Kısaltma")
    savedate=models.DateTimeField(auto_now_add= True,verbose_name="Eklenme Tarihi")
    def __str__(self):
        return self.name
    
    
class Movies_Table(models.Model):
    movieID=models.CharField(max_length=100,verbose_name="ID",)
    name=models.CharField(max_length=100,verbose_name="İsim")
    url_name=models.CharField(max_length=100,verbose_name="Url İsmi")
    production=models.CharField(max_length=100,verbose_name="Yapımcı")
    about=models.TextField(verbose_name="Hakkında")
    category_id = models.ManyToManyField(category_movie, verbose_name="Tür")
    release=models.DateTimeField(verbose_name="Çıkış Tarihi")
    imdb=models.IntegerField(verbose_name="IMDB")
    metacritic=models.IntegerField(verbose_name="Metacritic")
    background=models.CharField(max_length=500,verbose_name="Arkaplan")
    poster=models.CharField(max_length=500,verbose_name="Poster")
    trailer=models.CharField(max_length=500,verbose_name="Trailer")
    savedate=models.DateTimeField(auto_now_add= True,verbose_name="Eklenme Tarihi")
    isPublished=models.BooleanField(default=True,verbose_name="Yayın Durumu")
    def __str__(self):
        return self.name