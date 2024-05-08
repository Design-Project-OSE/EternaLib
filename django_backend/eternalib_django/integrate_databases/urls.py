from django.urls import path
from . import views 

urlpatterns = [
    path('',views.index,name="movie"),
    path('<int:mov_id>',views.detail,name="detail"),
    path('search',views.search,name="search"),
]
