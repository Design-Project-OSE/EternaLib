from django.urls import path
from . import views

"""

models.py içerisinde tablolar bulunmaktadır.
views.py içerisinde fonksiyonlar bulunur 

http://127.0.0.1:8000 ana sayfa
http://127.0.0.1:8000/users/id id: Kullanıcı ID belli bir profile yönlendiriyor
http://127.0.0.1:8000/game/id/comment id:oyun id belli bir oyunun yorumlarına yönlendiriyor
http://127.0.0.1:8000/movie/id/comment id:film id belli bir filmin yorumlarına yönlendiriyor
http://127.0.0.1:8000/book/id/comment id:kitap id belli bir kitabın yorumlarına yönlendiriyor

!!!!EKLENMEDİ!!!
http://127.0.0.1:8000/game/id/like id:kullanıcı id belli bir kullanıcının beğendiği oyunlar
http://127.0.0.1:8000/movie/id/like id:kullanıcı id belli bir kullanıcının beğendiği filmler
http://127.0.0.1:8000/book/id/like id:kullanıcı id belli bir kullanıcının beğendiği kitaplar
http://127.0.0.1:8000/users/id/game/comment userid: kullanıcı id id:oyun id 
belli bir kullanıcının oyun yorumlarını veriyor
http://127.0.0.1:8000/users/id/movie/comment userid: kullanıcı id:film id 
belli bir kullanıcının film yorumlarını veriyor
http://127.0.0.1:8000/users/id/book/comment userid: kullanıcı id:kitap id 
belli bir kullanıcının kitap yorumlarını veriyor

"""

urlpatterns=[
    path('users/<str : id>',views.list_userprofile),
    #Profil bilgilerini çekiyor
    
    path('users/',views.list_Users),
    #Kullanıcı bilgilerini çekiyor
    
    path('custom/users/',views.list_CustomUser),
    #Özelleştirilmiş bir kullanıcı oluşturur detay verilecek sonradan!!!!
    
    path('custom/users/manage',views.list_customusermanage),
    #Özelleştirilmiş kullanıcı ile ilgili detay verilecek!!!!
    
    path('book/comment',views.list_usersbookcomment),
    #Kitap yorumlarını çeker
    
    path('book/like',views.list_usersbooklike),
    #Beğenilen Kitapların bilgisini tutar
    
    path('game/comment',views.list_usersgamecomment),
    #Oyun yorumlarını tutar
    
    path('game/like',views.list_usersgamelike),
    #Beğenilen oyunların bilgisini tutar
    
    path('movie/comment',views.list_usersmoviecomment),
    #Film yorumları tutar
    
    path('movie/like',views.list_usersmovielike),
    #Beğenilen film bilgileri
    
    path('api/register/', views.list_register, name='register'),
    #Kayıt olan kullanıcının bilgisini çeker
]