from django.shortcuts import get_object_or_404
from rest_framework import permissions,status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from game.models import Games_Table
from game.serializers import Seri_gamestable
from movies.models import Movies_Table
from movies.serializers import Seri_movietable
from book.models import Book_Table
from book.serializers import Seri_booktable
from .form import searchform
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

@csrf_exempt
def search(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        form = searchform(data)
        if form.is_valid():
            search_term = form.cleaned_data['searchterm']
            movies = Movies_Table.objects.filter(name__icontains=search_term)
            books = Book_Table.objects.filter(name__icontains=search_term)
            games = Games_Table.objects.filter(name__icontains=search_term)
            sermov = Seri_movietable(movies, many=True)
            serbook = Seri_booktable(books, many=True)
            sergame = Seri_gamestable(games, many=True)
            return JsonResponse({'movies': sermov.data, 'books': serbook.data, 'games': sergame.data})
        else:
            return JsonResponse({'message': 'not success', 'errors': form.errors}, status=400)
    else:
        form = searchform()
        return JsonResponse({'form': form.errors}, status=400)