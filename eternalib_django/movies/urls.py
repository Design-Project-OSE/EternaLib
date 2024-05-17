from django.urls import path
from . import views 

urlpatterns = [
    path('movies/all',views.list_movie,name="movie"),
    path('movies/category',views.list_categorymovie,name="kategori"),
]
