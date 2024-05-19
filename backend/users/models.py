from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
import uuid

class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def save(self, *args, **kwargs):
        # Kullanıcı adını otomatik olarak oluştur
        if not self.username:
            self.username = self.first_name + '_' + self.last_name.replace(' ', '_')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email
    
class UserProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="Kullanıcı ID")
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    liked_movies = models.CharField(max_length=100)
    liked_games = models.CharField(max_length=100)
    liked_books = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_pics/')
    instagram_link = models.URLField(blank=True)
    facebook_link = models.URLField(blank=True)
    x_link= models.URLField(blank=True)
    linkedin_link = models.URLField(blank=True)
    about=models.TextField(verbose_name="Hakkında")

    def __str__(self):
        return self.user.username