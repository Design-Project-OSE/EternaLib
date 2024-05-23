from django.urls import path
from . import views
"""

models.py içerisinde tablolar bulunmaktadır.
views.py içerisinde fonksiyonlar bulunur 

http://127.0.0.1:8000 ana sayfa
http://127.0.0.1:8000/movies/ filmlerin özellikleri döner
http://127.0.0.1:8000/movie/category/ film kategorilerinin bilgilerini verir

http://127.0.0.1:8000/movies/id id:film ID verilen filmi verir

"""
urlpatterns=[
    path('movies',views.list_movie,name="Filmler"),
    path('movies/category',views.list_moviecategory,name="Film Kategorileri"),
    path('movies/comment',views.list_moviecomment,name="Film Yorumları"),
    path('movies/like',views.list_movielike,name="Film Beğenileri"),
    path('movies/id/<uuid:id>',views.list_movieid,name="Film id sayfası"),
    path('movies/urlname/<str:urlname>',views.list_movieurlname,name="Film id sayfası"),
    path('movies/add/comment',views.list_moviegetcomment,name="Yorum yapma"),
    path('movies/add/like',views.list_moviegetlike,name="Beğeni yapma"),
    path('movies/get/id/comment',views.list_getidcomments,name="POST olarak girilen movieID ait tüm yorumları çekiyor"),
    path('movies/get/mid/like',views.list_getidlikes,name="POST olarak girilen movieID ait tüm like çekiyor"),
    path('movies/get/uid/like',views.list_getidlikeusers,name="POST olarak girilen userID ait tüm like çekiyor"),
    path('movies/get/id/category/<uuid:id>',views.list_moviecategoryid,name="id girilen category bilgileri"),
    path('movies/like/search',views.list_liked,name="userID verilen kullanıcının  beğendiği filmler tam liste"),
    path('movies/list/top',views.list_mostmovies,name="[GET] ETKİ=[En iyi 5 filmi verir]  INPUTS=[]")
]