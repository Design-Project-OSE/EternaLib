from django.db import models
import uuid
maxurl=200
maxtext=100
maxrich=2000
maxtag=3

class Game_Comment(models.Model):
    id = id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,verbose_name="Oyun Yorum ID")
    userID=models.CharField(max_length=maxtext,verbose_name="Kullanıcı ID")
    gameID=models.CharField(max_length=maxtext,verbose_name="Oyun ID")
    comment=models.TextField(verbose_name="Yorum",max_length=maxrich)
    savedate=models.DateTimeField(auto_now_add= True,verbose_name="Eklenme Tarihi")
    class Meta:
        verbose_name = "Oyun Yorum"
        verbose_name_plural = "Oyun Yorum"

    def __str__(self):
        return str(self.id)
    
class Game_Like(models.Model):
    id=models.id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,verbose_name="Oyun Beğeni ID")
    userID=models.CharField(max_length=maxtext,verbose_name="Kullanıcı ID")
    gameID=models.CharField(max_length=maxtext,verbose_name="Oyun ID")
    like=models.BooleanField(verbose_name="beğeni")
    dislike=models.BooleanField(verbose_name="beğenmeme")
    savedate=models.DateTimeField(auto_now_add= True,verbose_name="Eklenme Tarihi")
    class Meta:
        verbose_name = "Oyun Beğeni"
        verbose_name_plural = "Oyun Beğenileri"

    def __str__(self):
        return str(self.id)
class Game_Category(models.Model):
    id=id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,verbose_name="Oyun Kategori ID")
    name=models.CharField(max_length=maxtext,verbose_name="Tür İsmi")
    catshort=models.CharField(max_length=maxtag,verbose_name="Tür Kısaltma")
    savedate=models.DateTimeField(auto_now_add= True,verbose_name="Eklenme Tarihi")
    class Meta:
        verbose_name = "Oyun Kategori"
        verbose_name_plural = "Oyun Kategorileri"

    def __str__(self):
        return self.name

class Games_Table(models.Model):
    id=id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,verbose_name="Oyun ID")
    name=models.CharField(max_length=maxtext,verbose_name="İsim")
    urlname=models.CharField(max_length=maxtext,verbose_name="URL İsmi")
    production=models.CharField(max_length=maxtext,verbose_name="Yapımcı")
    about=models.TextField(verbose_name="Hakkında",max_length=maxrich)
    categories = models.ManyToManyField(Game_Category, verbose_name="Tür")
    release=models.DateTimeField(verbose_name="Çıkış Tarihi")
    imdb=models.FloatField(verbose_name="IMDB")
    metacritic=models.FloatField(verbose_name="Metacritic")
    background=models.URLField(max_length=maxurl,verbose_name="Arkaplan URL")
    poster=models.URLField(max_length=maxurl,verbose_name="Poster URL")
    trailer=models.URLField(max_length=maxurl,verbose_name="Trailer URL")
    savedate=models.DateTimeField(auto_now_add= True,verbose_name="Eklenme Tarihi")
    isPublished=models.BooleanField(default=True,verbose_name="Yayın Durumu")
    like=models.IntegerField(default=0,verbose_name="Beğeni sayısı")
    dislike=models.IntegerField(default=0,verbose_name="Beğenilmeyen")
    class Meta:
        verbose_name = "Oyun"
        verbose_name_plural = "Oyunlar"

    def __str__(self):
        return self.name