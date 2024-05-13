from django.db import models
from django.contrib.auth.models import User,AbstractBaseUser, BaseUserManager

maxvalue=100

class Users_MovieLike(models.Model):
    userID=models.CharField(max_length=maxvalue,verbose_name="Kullanıcı_ID")
    movieID=models.CharField(max_length=maxvalue,verbose_name="Film ID")
    Like=models.BooleanField(default=False,verbose_name="Beğeni")
    savedate=models.DateTimeField(auto_now_add= True,verbose_name="Eklenme Tarihi")
    
class Users_BookLike(models.Model):
    userID=models.CharField(max_length=maxvalue,verbose_name="Kullanıcı_ID")
    bookID=models.CharField(max_length=maxvalue,verbose_name="Kitap ID")
    Like=models.BooleanField(default=False,verbose_name="Beğeni")
    savedate=models.DateTimeField(auto_now_add= True,verbose_name="Eklenme Tarihi")
    
class Users_GameLike(models.Model):
    userID=models.CharField(max_length=maxvalue,verbose_name="Kullanıcı_ID")
    gameID=models.CharField(max_length=maxvalue,verbose_name="Oyun ID")
    Like=models.BooleanField(default=False,verbose_name="Beğeni")
    savedate=models.DateTimeField(auto_now_add= True,verbose_name="Eklenme Tarihi")
    
class Users_MovieComment(models.Model):
    userID=models.CharField(max_length=maxvalue,verbose_name="Kullanıcı_ID")
    movieID=models.CharField(max_length=maxvalue,verbose_name="Film ID")
    comment=models.TextField(verbose_name="Yorum")
    savedate=models.DateTimeField(auto_now_add= True,verbose_name="Eklenme Tarihi")
    isPublished=models.BooleanField(default=True,verbose_name="Yayın Durumu")
    
class Users_BookComment(models.Model):
    userID=models.CharField(max_length=maxvalue,verbose_name="Kullanıcı_ID")
    bookID=models.CharField(max_length=maxvalue,verbose_name="Kitap ID")
    comment=models.TextField(verbose_name="Yorum")
    savedate=models.DateTimeField(auto_now_add= True,verbose_name="Eklenme Tarihi")
    isPublished=models.BooleanField(default=True,verbose_name="Yayın Durumu")
    
class Users_GameComment(models.Model):
    userID=models.CharField(max_length=maxvalue,verbose_name="Kullanıcı_ID")
    gameID=models.CharField(max_length=maxvalue,verbose_name="Oyun ID")
    comment=models.TextField(verbose_name="Yorum")
    savedate=models.DateTimeField(auto_now_add= True,verbose_name="Eklenme Tarihi")
    isPublished=models.BooleanField(default=True,verbose_name="Yayın Durumu")
    


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
class CustumUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)
    
class CustumUser(AbstractBaseUser):
    email=models.EmailField(unique=True,verbose_name="E-mail")
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustumUserManager()

    def __str__(self):
        return self.email
    

    