from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from .models import category_movie, Movies_Table
from .serializers import Seri_categorymovie,Seri_movietable


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def list_movie(request):
    movies=Movies_Table.objects.all()
    seri_movies=Seri_movietable(movies,many=True)
    return Response(seri_movies.data)

#catmov=category_movie
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def list_categorymovie(request):
    catmov=category_movie.objects.all()
    seri_catmov=Seri_categorymovie(catmov,many=True)
    return Response(seri_catmov.data)
