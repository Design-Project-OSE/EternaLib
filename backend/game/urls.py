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
    path('games/',views.list_game),
    path('games/category/',views.list_categorygames),
]