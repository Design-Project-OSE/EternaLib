from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid

class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,verbose_name="ID")  
    full_name = models.CharField(max_length=255,verbose_name="İsim Soyad")
    email = models.EmailField(unique=True,verbose_name="E-Mail")
    username = models.CharField(max_length=150, unique=True,blank=True, null=True,verbose_name="Kullanıcı Adı")
    password = models.CharField(max_length=128,verbose_name="Şifre")
    x_link = models.URLField(blank=True, null=True,verbose_name="X URL")
    instagram_link = models.URLField(blank=True, null=True,verbose_name="İnstegram URL")
    facebook_link = models.URLField(blank=True, null=True,verbose_name="Facebook URL")
    linkedin_link = models.URLField(blank=True, null=True,verbose_name="Linkedn URL")
    savedate=models.DateTimeField(auto_now=True,verbose_name="Kayıt Tarihi")

    def __str__(self):
        return self.email