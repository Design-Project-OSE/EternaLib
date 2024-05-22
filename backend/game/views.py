from django.shortcuts import get_object_or_404
from rest_framework import permissions,status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from .models import Games_Table,Game_Like,Game_Comment,Game_Category
from .serializers import Seri_gamestable,Seri_gamescategory,Seri_gamescomment,Seri_gameslike
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

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
def list_gamecategoryid(request,id):
    obj=get_object_or_404(Game_Category,id=id)
    seri=Seri_gamescategory(obj)
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
            game_comment=serializer.save()
            game = get_object_or_404(Games_Table, id=game_comment.gameID)
            if game_comment.commentscount:
                game.commentscount+=1
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
        data = json.loads(request.body.decode('utf-8'))
        serializer = Seri_gameslike(data=data)
        if serializer.is_valid():
            user_id = serializer.validated_data['userID']
            game_id = serializer.validated_data['gameID']
            game = get_object_or_404(Games_Table, id=game_id)
            like = serializer.validated_data['like']
            dislike = serializer.validated_data['dislike']
            existing_like = Game_Like.objects.filter(userID=user_id, gameID=game_id).first()
            
            if existing_like:
                game = get_object_or_404(Games_Table, id=game_id)
                if existing_like.like and not like:
                    game.like -= 1
                if existing_like.dislike and not dislike:
                    game.dislike -= 1
                if not existing_like.like and like:
                    game.like += 1
                if not existing_like.dislike and dislike:
                    game.dislike += 1
                existing_like.like = like
                existing_like.dislike = dislike
                existing_like.save()
                game.save()
                
                return JsonResponse({**data,  "likecount": game.like, "dislikecount": game.dislike,'like':like,'dislike':dislike}, status=status.HTTP_200_OK)

            game_like = serializer.save()
            
            if game_like.like:
                game.like += 1
            if game_like.dislike:
                game.dislike += 1
            game.save()
            
            return JsonResponse({**data, "likecount": game.like, "dislikecount": game.dislike,'like':like,'dislike':dislike}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@csrf_exempt
def list_getidcomments(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        game_id = data.get('gameID')
        if game_id is not None:  
            comments = Game_Comment.objects.filter(gameID=game_id)
            serializer = Seri_gamescomment(comments, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse({'error': 'No game ID provided.'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed.'}, status=405)
    
@csrf_exempt
def list_getidlikes(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        game_id = data.get('gameID')
        if game_id is not None:  
            comments = Game_Like.objects.filter(gameID=game_id)
            serializer = Seri_gameslike(comments, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse({'error': 'No game ID provided.'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed.'}, status=405)
    
def list_getidlikeusers(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        user_id = data.get('userID')
        if user_id is not None:  
            likes = Game_Like.objects.filter(user_id=user_id)
            serializer = Seri_gameslike(likes, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse({'error': 'No user ID provided.'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed.'}, status=405)