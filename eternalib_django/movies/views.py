from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Movies_Genres_Table, Movies_Table
from .serilaziers import Seri_Genres,Seri_Movie


@api_view('GET')
def list_movie(request):
    movies=Movies_Table.objects.all()
    seri_movies=Seri_Movie(movies,many=True)
    return Response(seri_movies.data)

#catmov=category_movie
@api_view('GET')
def list_categorymovie(request):
    catmov=Movies_Genres_Table.objects.all()
    seri_catmov=Seri_Genres(catmov,many=True)
    return Response(seri_catmov.data)
