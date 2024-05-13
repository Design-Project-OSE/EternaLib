from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse,JsonResponse

from movies.models import Movies_Table,Movies_Genres_Table
from eternalib_django.serializers import Movies_TableSerializers,Movies_Genres_TableSerializers

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def movie_get_data(request):
    movie_data= Movies_Table.objects.all()
    if request.method=='GET':
        serializer=Movies_TableSerializers(movie_data,many=True)
        return JsonResponse(serializer.data,safe=False)

@csrf_exempt
def genmovie_get_data(request):
    genmovie_data= Movies_Genres_Table.objects.all()
    if request.method=='GET':
        serializer=Movies_Genres_TableSerializers(genmovie_data,many=True)
        return JsonResponse(serializer.data,safe=False)