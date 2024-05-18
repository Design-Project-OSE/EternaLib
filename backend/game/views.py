from django.shortcuts import get_object_or_404
from rest_framework import permissions,status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from .models import Games_Table,Game_Like,Game_Comment,Game_Category
from .serializers import Seri_gamestable,Seri_gamescategory,Seri_gamescomment,Seri_gameslike


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def list_game(request):
    obj=Games_Table.objects.all()
    seri=Seri_gamestable(obj,many=True)
    return Response(seri.data)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def list_gamecategory(request):
    obj=Game_Category.objects.all()
    seri=Seri_gamescategory(obj,many=True)
    return Response(seri.data)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def list_gamecomment(request):
    obj=Game_Comment.objects.all()
    seri=Seri_gamescomment(obj,many=True)
    return Response(seri.data)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def list_gamelike(request):
    obj=Game_Like.objects.all()
    seri=Seri_gameslike(obj,many=True)
    return Response(seri.data)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def list_gameid(request,id):
    obj=get_object_or_404(Games_Table,id=id)
    seri=Seri_gamestable(obj)
    return Response(seri.data)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def list_gameurlname(request,urlname):
    obj=get_object_or_404(Games_Table,urlname=urlname)
    seri=Seri_gamestable(obj)
    return Response(seri.data)

@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def list_gamegetcomment(request):
    if request.method == 'GET':
        comments = Game_Comment.objects.all()
        serializer = Seri_gamescomment(comments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = Seri_gamescomment(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
@permission_classes([permissions.AllowAny])
def list_gamegetlike(request):
    if request.method == 'GET':
        likes = Game_Like.objects.all()
        serializer = Seri_gameslike(likes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = Seri_gameslike(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)