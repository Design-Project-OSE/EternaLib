from django.urls import path
from . import views 

urlpatterns = [
    path('movies/all',views.index,name="movie"),
]
