from django.shortcuts import get_object_or_404
from rest_framework import permissions,status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from .models import Movies_Table,Movies_Comment,Movies_Category,Movies_Like
from .serializers import Seri_movietable,Seri_moviecategory,Seri_moviecomment,Seri_movielike


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def list_movie(request):
    obj=Movies_Table.objects.all()
    seri=Seri_movietable(obj,many=True)
    return Response(seri.data)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def list_moviecategory(request):
    obj=Movies_Category.objects.all()
    seri=Seri_moviecategory(obj,many=True)
    return Response(seri.data)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def list_moviecomment(request):
    obj=Movies_Comment.objects.all()
    seri=Seri_moviecomment(obj,many=True)
    return Response(seri.data)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def list_movielike(request):
    obj=Movies_Like.objects.all()
    seri=Seri_movielike(obj,many=True)
    return Response(seri.data)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def list_movieid(request,id):
    obj=get_object_or_404(Movies_Table,id=id)
    seri=Seri_movietable(obj)
    return Response(seri.data)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def list_movieurlname(request,urlname):
    obj=get_object_or_404(Movies_Table,urlname=urlname)
    seri=Seri_movietable(obj)
    return Response(seri.data)



@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def list_moviegetcomment(request):
    if request.method == 'GET':
        comments = Movies_Comment.objects.all()
        serializer = Seri_moviecomment(comments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = Seri_moviecomment(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
@permission_classes([permissions.AllowAny])
def list_moviegetlike(request):
    if request.method == 'GET':
        likes = Movies_Like.objects.all()
        serializer = Seri_movielike(likes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = Seri_movielike(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)