from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from .models import Movies_Genres_Table, Movies_Table
from .serilaziers import Seri_Genres, Seri_Movie

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def list_movie(request):
    queryset = Movies_Table.objects.all()  # Movies_Table için queryset belirle
    seri_movies = Seri_Movie(queryset, many=True)
    return Response(seri_movies.data)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def list_categorymovie(request):
    queryset = Movies_Genres_Table.objects.all()  # Movies_Genres_Table için queryset belirle
    seri_catmov = Seri_Genres(queryset, many=True)
    return Response(seri_catmov.data)
