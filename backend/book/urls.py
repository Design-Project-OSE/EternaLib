from django.urls import path
from . import views

"""

models.py içerisinde tablolar bulunmaktadır.
views.py içerisinde fonksiyonlar bulunur 

http://127.0.0.1:8000 ana sayfa
http://127.0.0.1:8000/book/ kitapların özellikleri döner
http://127.0.0.1:8000/book/category/ kitap kategorilerinin bilgilerini verir
!!!EKLENMEDİ!!!
http://127.0.0.1:8000/book/id id:kitap ID verilen kitabı verir

"""
urlpatterns=[
    path('book/',views.list_booktable,name='Kitap Anasayfa'),
    path('book/category/',views.list_bookcategory,name='Kitap Kategorileri'),
    path('book/comments/',views.list_bookcomment,name='Kitap Yorumları'),
    path('book/like/',views.list_booklike,name='Kitap Beğenenler'),
    path('book/id/<int:id>/', views.list_bookid, name="Oyun ID Çekme"),
    path('book/urlname/<str:urlname>/', views.list_bookurlname, name="Oyun URL Çekme"),
    path('book/get/comment',views.list_bookgetcomment,name="Yorum yapma"),
    path('book/get/like/get',views.list_bookgetlike,name="Beğeni yapma"),
]