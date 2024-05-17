from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from .models import category_game,Games_Table
from .serializers import Seri_category_games,Seri_gamestable


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def list_game(request):
    movies=Games_Table.objects.all()
    seri_movies=Seri_gamestable(movies,many=True)
    return Response(seri_movies.data)

#catmov=category_movie
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def list_categorygames(request):
    catmov=category_game.objects.all()
    seri_catmov=Seri_category_games(catmov,many=True)
    return Response(seri_catmov.data)
