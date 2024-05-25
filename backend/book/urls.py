from django.urls import path
from . import views

"""

models.py içerisinde tablolar bulunmaktadır.
views.py içerisinde fonksiyonlar bulunur 

http://127.0.0.1:8000 ana sayfa
http://127.0.0.1:8000/book/ kitapların özellikleri döner
http://127.0.0.1:8000/book/category/ kitap kategorilerinin bilgilerini verir
http://127.0.0.1:8000/book/id id:kitap ID verilen kitabı verir

"""
urlpatterns=[
    path('books',views.list_booktable,name='Kitap Anasayfa'),
    path('books/category',views.list_bookcategory,name='Kitap Kategorileri'),
    path('books/category/get',views.list_getcategory,name="categoryID alıyor tüm sahip kitapları çekiyor"),
    path('books/comments',views.list_bookcomment,name='Kitap Yorumları'),
    path('books/comment/delete',views.delete_comment,name="Oyun Yorumlarını siler commentID"),
    path('books/like',views.list_booklike,name='Kitap Beğenenler'),
    path('books/id/<uuid:id>', views.list_bookid, name="Oyun ID Çekme"),
    path('books/urlname/<str:urlname>', views.list_bookurlname, name="Oyun URL Çekme"),
    path('books/add/comment',views.list_bookgetcomment,name="Yorum yapma"),
    path('books/add/like',views.list_bookgetlike,name="Beğeni yapma"),
    path('books/get/id/comment',views.list_getidcomments,name="POST olarak girilen bookID ait tüm yorumları çekiyor"),
    path('books/get/id/category/<uuid:id>',views.list_bookcategoryid,name="id girilen category bilgileri"),
    path('books/get/gid/like',views.list_getidlikes,name="POST olarak girilen bookID ait tüm like çekiyor"),
    path('books/get/sid/like',views.list_getidlikeusers,name="POST olarak girilen userID ait tüm like çekiyor"),
    path('books/list/top',views.list_mostbooks,name="[GET] ETKİ=[En iyi 5 filmi verir]  INPUTS=[]"),
    path('books/like/search',views.list_liked,name="userID verilen kullanıcının  beğendiği kitaplar tam liste"),
    
]