from rest_framework import serializers, ModelSerializer
from .models import UserProfile,Users_BookComment,Users_BookLike,Users_GameComment,Users_GameLike,Users_MovieComment,User,Users_MovieLike,CustumUserManager,CustumUser

class Seri_userprofile(ModelSerializer):
    class meta:
        model=UserProfile
        fields=('__all__',)
        
class Seri_userbookcomment(ModelSerializer):
    class meta:
        model=Users_BookComment
        fields=('__all__')
        
class Seri_usersbooklike(ModelSerializer):
    class meta:
        model=Users_BookLike
        fields=('__all__')
        
class Seri_usersgamecomment(ModelSerializer):
    class meta:
        model=Users_GameComment
        fields=('__all__')
        
class Seri_usersgamelike(ModelSerializer):
    class meta:
        model=Users_GameLike
        fields=('__all__')
        
class Seri_usersmoviecomment(ModelSerializer):
    class meta:
        model=Users_MovieComment
        fields=('__all__')
        

class Seri_users(ModelSerializer):
    class meta:
        model=User
        fields=('__all__')        
        

class Seri_usersmovielike(ModelSerializer):
    class meta:
        model=Users_MovieLike
        fields=('__all__')  
        
class Seri_customuser(ModelSerializer):
    class meta:
        model=CustumUser
        fields=('__all__')  
        
class Seri_customusermanage(ModelSerializer):
    class meta:
        model=CustumUserManager
        fields=('__all__')  
        