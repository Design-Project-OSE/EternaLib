from django.db import models
import uuid

maxurl = 200
maxtext = 100
maxrich = 2000
maxtag = 3

class Book_Comment(models.Model):
    id = id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="Kitap Yorum ID")
    userID = models.CharField(max_length=maxtext, verbose_name="Kullanıcı ID")
    bookID = models.CharField(max_length=maxtext, verbose_name="Kitap ID")
    comment = models.TextField(verbose_name="Yorum", max_length=maxrich)  
    savedate = models.DateTimeField(auto_now_add=True, verbose_name="Eklenme Tarihi")

    class Meta:
        verbose_name = "Kitap Yorum"
        verbose_name_plural = "Kitap Yorumları"

    def __str__(self):
        return self.comment 

class Book_Like(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="Kitap Beğeni ID")
    userID = models.CharField(max_length=maxtext, verbose_name="Kullanıcı ID")
    bookID = models.CharField(max_length=maxtext, verbose_name="Kitap ID")
    like=models.BooleanField(verbose_name="beğeni")
    dislike=models.BooleanField(verbose_name="beğenmeme")
    savedate = models.DateTimeField(auto_now_add=True, verbose_name="Eklenme Tarihi")

    class Meta:
        verbose_name = "Kitap Beğeni"
        verbose_name_plural = "Kitap Beğenileri"


    def __str__(self):
        return f"Beğeni ID: {self.id}"  

class Book_Category(models.Model):
    id = id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="Kitap Kategori ID")
    name = models.CharField(max_length=maxtext, verbose_name="Tür İsmi")
    catshort = models.CharField(max_length=maxtag, verbose_name="Kitap Türü Kısaltması")
    savedate = models.DateTimeField(auto_now_add=True, verbose_name="Eklenme Tarihi")

    class Meta:
        verbose_name = "Kitap Kategori"
        verbose_name_plural = "Kitap Kategorileri"

    def __str__(self):
        return self.name  

class Book_Table(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="Kitap ID")
    name = models.CharField(max_length=maxtext, verbose_name="İsim")
    urlname = models.CharField(max_length=maxtext, verbose_name="URL İsmi")
    production = models.CharField(max_length=maxtext, verbose_name="Yapımcı")
    about = models.TextField(verbose_name="Hakkında", max_length=maxrich)
    categories = models.ManyToManyField(Book_Category, verbose_name="Tür")
    release = models.DateTimeField(verbose_name="Çıkış Tarihi")
    background = models.URLField(max_length=maxurl, verbose_name="Arkaplan URL")
    poster = models.URLField(max_length=maxurl, verbose_name="Poster URL")
    savedate = models.DateTimeField(auto_now_add=True, verbose_name="Eklenme Tarihi")
    isPublished = models.BooleanField(default=True, verbose_name="Yayın Durumu")
    like = models.IntegerField(verbose_name="Beğeni Sayısı")  
    dislike=models.IntegerField(verbose_name="Beğenilmeyen")  
    commentscount=models.IntegerField(verbose_name="Yorum sayısı")  

    class Meta:
        verbose_name = "Kitap"
        verbose_name_plural = "Kitaplar"
        

    def __str__(self):
        return self.name  
