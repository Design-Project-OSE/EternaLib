from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import category_book,Book_Table
from .serializers import Seri_booktable,Seri_categorybook

#obj= tüm objectleri tutar
#seri=obj response için seriliazer uygular
@api_view('GET')
def list_categorybook(request):
    obj=category_book.objects.all()
    seri=Seri_categorybook(obj,many=True)
    return Response(seri.data)

#obj= tüm objectleri tutar
#seri=obj response için seriliazer uygular
@api_view('GET')
def list_booktable(request):
    obj=Book_Table.objects.all()
    seri=Seri_booktable(obj,many=True)
    return Response(seri.data)