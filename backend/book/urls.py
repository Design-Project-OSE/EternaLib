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
    path('book/',views.list_booktable),
    path('book/category/',views.list_categorybook),
]