from django.shortcuts import get_object_or_404
from rest_framework import permissions
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