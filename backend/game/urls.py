from django.urls import path
from . import views

"""

models.py içerisinde tablolar bulunmaktadır.
views.py içerisinde fonksiyonlar bulunur 

http://127.0.0.1:8000 ana sayfa
http://127.0.0.1:8000/games/ oyun özellikleri döner
http://127.0.0.1:8000/games/category/ oyun kategorilerinin bilgilerini verir

http://127.0.0.1:8000/games/id id:oyun ID verilen filmi verir

"""
urlpatterns=[
    path('games',views.list_game,name="Oyunlar"),
    path('games/category',views.list_gamecategory,name="Oyun Kategorileri"),
    path('games/comment',views.list_gamecomment,name="Oyun Yorumları"),
    path('games/comment/delete',views.delete_comment,name="Oyun Yorumlarını siler commentID"),
    path('games/like',views.list_gamelike,name="Oyun Beğenileri"),
    path('games/id/<uuid:id>', views.list_gameid, name="Oyun ID Çekme"),
    path('games/urlname/<str:urlname>', views.list_gameurlname, name="Oyun URL Çekme"),
    path('games/add/comment',views.list_gamegetcomment,name="Yorum yapma"),
    path('games/add/like',views.list_gamegetlike,name="Beğeni yapma"),
    path('games/get/id/category/<uuid:id>', views.list_gamecategoryid, name="id girilen category bilgileri"),
    path('games/get/id/comment',views.list_getidcomments,name="POST olarak girilen gameID ait tüm yorumları çekiyor"),
    path('games/get/gid/like',views.list_getidlikes,name="POST olarak girilen gameID ait tüm like çekiyor"),
    path('games/get/sid/like',views.list_getidlikeusers,name="POST olarak girilen userID ait tüm like çekiyor"),
    path('games/get/id/category/<uuid:id>',views.list_gamecategoryid,name="id girilen category bilgileri"),
    path('games/like/search',views.list_liked,name="userID verilen kullanıcının  beğendiği oyunlar tam liste"),
    path('games/list/top',views.list_mostgames,name="[GET] ETKİ=[En iyi 5 oyun verir]  INPUTS=[]"),
    path('games/category/get',views.list_getcategory,name="categoryID alıyor tüm sahip kitapları çekiyor")
]