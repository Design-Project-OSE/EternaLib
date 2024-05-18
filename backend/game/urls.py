from django.urls import path
from . import views

"""

models.py içerisinde tablolar bulunmaktadır.
views.py içerisinde fonksiyonlar bulunur 

http://127.0.0.1:8000 ana sayfa
http://127.0.0.1:8000/games/ oyun özellikleri döner
http://127.0.0.1:8000/games/category/ oyun kategorilerinin bilgilerini verir
!!!EKLENMEDİ!!!
http://127.0.0.1:8000/games/id id:oyun ID verilen filmi verir

"""
urlpatterns=[
    path('games/',views.list_game,name="Oyunlar"),
    path('games/category/',views.list_gamecategory,name="Oyun Kategorileri"),
    path('games/comment/',views.list_gamecomment,name="Oyun Yorumları"),
    path('games/like/',views.list_gamelike,name="Oyun Beğenileri"),
    path('games/id/<int:id>/', views.list_gameid, name="Oyun ID Çekme"),
    path('games/urlname/<str:urlname>/', views.list_gameurlname, name="Oyun URL Çekme"),
    path('games/get/comment',views.list_gamegetcomment,name="Yorum yapma"),
    path('games/get/like',views.list_gamegetlike,name="Beğeni yapma"),
]