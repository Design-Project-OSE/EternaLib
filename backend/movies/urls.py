from django.urls import path
from . import views
"""

models.py içerisinde tablolar bulunmaktadır.
views.py içerisinde fonksiyonlar bulunur 

http://127.0.0.1:8000 ana sayfa
http://127.0.0.1:8000/movies/ filmlerin özellikleri döner
http://127.0.0.1:8000/movie/category/ film kategorilerinin bilgilerini verir
!!!EKLENMEDİ!!!
http://127.0.0.1:8000/movies/id id:film ID verilen filmi verir

"""
urlpatterns=[
    path('movies/',views.list_movie,name="Filmler"),
    path('movie/category/',views.list_moviecategory,name="Film Kategorileri"),
    path('movies/comment/',views.list_moviecomment,name="Film Yorumları"),
    path('movies/like/',views.list_movielike,name="Film Beğenileri"),
    path('movies/id/<int:id>/',views.list_movieid,name="Film id sayfası"),
    path('movies/id/<str:urlname>/',views.list_movieurlname,name="Film id sayfası"),
]