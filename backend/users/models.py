from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid

class CustomUser(AbstractUser):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="Kullanıcı ID")
    email = models.EmailField(_('email address'), unique=True)
    namesurname = models.CharField(max_length=255, verbose_name="Name Surname")
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    def get_full_name(self):
       
        return self.first_name+' '+self.last_name
    def save(self, *args, **kwargs):
        
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

# Kullanıcı oluşturulduğunda tetiklenecek sinyal dinleyicisi
@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        full_name = instance.first_name + ' ' + instance.last_name
        UserProfile.objects.create(user=instance, full_name=full_name)

# Kullanıcı profili güncellendiğinde tetiklenecek sinyal dinleyicisi
@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
