from rest_framework import serializers
from .models import UserProfile,Users_BookComment,Users_BookLike,Users_GameComment,Users_GameLike,Users_MovieComment,User,Users_MovieLike,CustumUserManager,CustumUser

class Seri_userprofile():
    class meta:
        model=UserProfile
        fields=('__all__',)
        
class Seri_userbookcomment():
    class meta:
        model=Users_BookComment
        fields=('__all__')
        
class Seri_usersbooklike():
    class meta:
        model=Users_BookLike
        fields=('__all__')
        
class Seri_usersgamecomment():
    class meta:
        model=Users_GameComment
        fields=('__all__')
        
class Seri_usersgamelike():
    class meta:
        model=Users_GameLike
        fields=('__all__')
        
class Seri_usersmoviecomment():
    class meta:
        model=Users_MovieComment
        fields=('__all__')
        

class Seri_users():
    class meta:
        model=User
        fields=('__all__')        
        

class Seri_usersmovielike():
    class meta:
        model=Users_MovieLike
        fields=('__all__')  
        
class Seri_customuser():
    class meta:
        model=CustumUser
        fields=('__all__')  
        
class Seri_customusermanage():
    class meta:
        model=CustumUserManager
        fields=('__all__')  
        