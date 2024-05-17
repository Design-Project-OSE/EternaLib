from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from rest_framework.status import status
from .models import User,CustumUserManager,CustumUser,UserProfile,Users_BookComment,Users_BookLike,Users_GameComment,Users_GameLike,Users_MovieComment,Users_MovieLike
from .serializers import Seri_users,Seri_userprofile,Seri_customuser,Seri_customusermanage,Seri_userbookcomment,Seri_usersbooklike,Seri_usersgamecomment,Seri_usersgamelike,Seri_usersmoviecomment,Seri_usersmovielike

#obj= tüm objectleri tutar
#seri=obj response için seriliazer uygular
@api_view(['GET'])
def list_CustomUser(request):
    obj=CustumUser.objects.all()
    seri=Seri_customuser(obj,many=True)
    return Response(seri.data)

@api_view(['GET'])
def list_Users(request):
    obj=User.objects.all()
    seri=Seri_users(obj,many=True)
    return Response(seri.data)

@api_view(['GET'])
def list_customusermanage(request):
    obj=CustumUserManager.objects.all()
    seri=Seri_customusermanage(obj,many=True)
    return Response(seri.data)

@api_view(['GET'])
def list_userprofile(request):
    obj=UserProfile.objects.all()
    seri=Seri_userprofile(obj,many=True)
    return Response(seri.data)

@api_view(['GET'])
def list_usersbookcomment(request):
    obj=Users_BookComment.objects.all()
    seri=Seri_userbookcomment(obj,many=True)
    return Response(seri.data)

@api_view(['GET'])
def list_usersbooklike(request):
    obj=Users_BookLike.objects.all()
    seri=Seri_usersbooklike(obj,many=True)
    return Response(seri.data)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def list_usersgamecomment(request):
    obj=Users_GameComment.objects.all()
    seri=Seri_usersgamecomment(obj,many=True)
    return Response(seri.data)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def list_usersgamelike(request):
    obj=Users_GameLike.objects.all()
    seri=Seri_usersgamelike(obj,many=True)
    return Response(seri.data)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def list_usersmoviecomment(request):
    obj=Users_MovieComment.objects.all()
    seri=Seri_usersmoviecomment(obj,many=True)
    return Response(seri.data)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def list_usersmovielike(request):
    obj=Users_MovieLike.objects.all()
    seri=Seri_usersmovielike(obj,many=True)
    return Response(seri.data)

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def list_register(request):
    seri=Seri_users(data=request.data)
    if seri.is_valid():
        seri.save()
        return Response(seri.data,status=status.HTTP_201_CREATED)
    return Response(seri.errors, status=status.HTTP_400_BAD_REQUEST)