from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from .models import Book_Table,Book_Category,Book_Like,Book_Comment
from .serializers import Seri_booktable,Seri_bookcategory,Seri_bookcomment,Seri_booklike

#obj= tüm objectleri tutar
#seri=obj response için seriliazer uygular
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def list_bookcategory(request):
    obj=Book_Category.objects.all()
    seri=Seri_bookcategory(obj,many=True)
    return Response(seri.data)

#obj= tüm objectleri tutar
#seri=obj response için seriliazer uygular
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def list_booktable(request):
    obj=Book_Table.objects.all()
    seri=Seri_booktable(obj,many=True)
    return Response(seri.data)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def list_bookcomment(request):
    obj=Book_Comment.objects.all()
    seri=Seri_bookcomment(obj,many=True)
    return Response(seri.data)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def list_booklike(request):
    obj=Book_Like.objects.all()
    seri=Seri_booklike(obj,many=True)
    return Response(seri.data)