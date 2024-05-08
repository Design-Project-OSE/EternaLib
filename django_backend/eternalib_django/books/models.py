from django.db import models

class Books_Genres_Table(models.Model):
    name=models.CharField(max_length=25,verbose_name="Tür İsmi")
    gen_id=models.CharField(max_length=2,verbose_name="Tür Kısaltma")
    savedate=models.DateTimeField(auto_now_add= True,verbose_name="Eklenme Tarihi")
    def __str__(self):
        return self.name

class Books_Table(models.Model):
    name=models.CharField(max_length=100,verbose_name="İsim")
    production=models.CharField(max_length=100,verbose_name="Yapımcı")
    about=models.TextField(verbose_name="Hakkında")
    genres = models.ManyToManyField(Books_Genres_Table, verbose_name="Tür")
    release=models.DateTimeField(verbose_name="Çıkış Tarihi")
    background=models.CharField(max_length=500,verbose_name="Arkaplan")
    poster=models.CharField(max_length=500,verbose_name="Poster")
    savedate=models.DateTimeField(auto_now_add= True,verbose_name="Eklenme Tarihi")
    isPublished=models.BooleanField(default=True,verbose_name="Yayın Durumu")
    def __str__(self):
        return self.name
