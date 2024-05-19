from django.db import models
from django.contrib.auth.models import User

class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username
    
class UserProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="Kullanıcı ID")
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    favorite_movie = models.CharField(max_length=100)
    favorite_game = models.CharField(max_length=100)
    favorite_book = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_pics/')
    instagram_link = models.URLField(blank=True)
    facebook_link = models.URLField(blank=True)
    linkedin_link = models.URLField(blank=True)

    def __str__(self):
        return self.user.username