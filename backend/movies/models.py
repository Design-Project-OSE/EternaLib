from django.db import models
import uuid


maxurl = 200
maxtext = 100
maxrich = 2000
maxtag = 3

class Movies_Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="Film Yorum ID")
    userID = models.CharField(max_length=maxtext, verbose_name="Kullanıcı ID")
    movieID = models.CharField(max_length=maxtext, verbose_name="Film ID")
    comment = models.TextField(verbose_name="Yorum", max_length=maxrich)
    savedate = models.DateTimeField(auto_now_add=True, verbose_name="Eklenme Tarihi")

    class Meta:
        verbose_name = "Film Yorum"
        verbose_name_plural = "Film Yorumları"

    def __str__(self):
        return self.comment

class Movies_Like(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="Film Beğeni ID")
    userID = models.CharField(max_length=maxtext, verbose_name="Kullanıcı ID")
    movieID = models.CharField(max_length=maxtext, verbose_name="Film ID")
    like=models.BooleanField(verbose_name="beğeni")
    dislike=models.BooleanField(verbose_name="beğeni")
    savedate = models.DateTimeField(auto_now_add=True, verbose_name="Eklenme Tarihi")

    class Meta:
        verbose_name = "Film Beğeni"
        verbose_name_plural = "Film Beğenileri"

    def __str__(self):
        return f"Beğeni ID: {self.movieID}"

class Movies_Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="Film Kategori ID")
    name = models.CharField(max_length=maxtext, verbose_name="Tür İsmi")
    catshort = models.CharField(max_length=maxtag, verbose_name="Tür Kısaltma")
    savedate = models.DateTimeField(auto_now_add=True, verbose_name="Eklenme Tarihi")

    class Meta:
        verbose_name = "Film Kategori"
        verbose_name_plural = "Film Kategorileri"

    def __str__(self):
        return self.name

class Movies_Table(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="Film ID")
    name = models.CharField(max_length=maxtext, verbose_name="İsim")
    urlname = models.CharField(max_length=maxtext, verbose_name="Url İsmi")
    production = models.CharField(max_length=maxtext, verbose_name="Yapımcı")
    about = models.TextField(max_length=maxrich, verbose_name="Hakkında")
    categories = models.ManyToManyField(Movies_Category, verbose_name="Kategoriler")  
    release = models.DateTimeField(verbose_name="Çıkış Tarihi")
    imdb = models.FloatField(verbose_name="IMDB")
    metacritic = models.FloatField(verbose_name="Metacritic")
    background = models.URLField(max_length=maxurl, verbose_name="Arkaplan URL")
    poster = models.URLField(max_length=maxurl, verbose_name="Poster URL")
    trailer = models.URLField(max_length=maxurl, verbose_name="Trailer URL")
    savedate = models.DateTimeField(auto_now_add=True, verbose_name="Eklenme Tarihi")
    isPublished = models.BooleanField(default=True, verbose_name="Yayın Durumu")
    like = models.IntegerField(verbose_name="Beğeniler")  
    dislike= models.IntegerField(verbose_name="Beğenilmeyenler")  
    class Meta:
        verbose_name = "Film"
        verbose_name_plural = "Filmler"

    def __str__(self):
        return self.name
