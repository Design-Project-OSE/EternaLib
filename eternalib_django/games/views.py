from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse,JsonResponse

from games.models import Games_Table,Games_Genres_Table
from eternalib_django.serializers import Games_TableSerializers,Games_Genres_TableSerializers

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def games_get_data(request):
    game_data= Games_Table.objects.all()
    if request.method=='GET':
        serializer=Games_TableSerializers(game_data,many=True)
        return JsonResponse(serializer.data,safe=False)

@csrf_exempt
def gengames_get_data(request):
    gengame_data= Games_Genres_Table.objects.all()
    if request.method=='GET':
        serializer=Games_Genres_TableSerializers(gengames_get_data,many=True)
        return JsonResponse(serializer.data,safe=False)