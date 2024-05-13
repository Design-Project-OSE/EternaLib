from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse,JsonResponse

from books.models import Books_Table,Books_Genres_Table
from eternalib_django.serializers import Books_TableSerializers,Books_Genres_TableSerializers

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def books_get_data(request):
    books_data= Books_Table.objects.all()
    if request.method=='GET':
        serializer=Books_TableSerializers(books_data,many=True)
        return JsonResponse(serializer.data,safe=False)

@csrf_exempt
def genbooks_get_data(request):
    genbook_data= Books_Genres_Table.objects.all()
    if request.method=='GET':
        serializer=Books_Genres_TableSerializers(genbook_data,many=True)
        return JsonResponse(serializer.data,safe=False)