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
from account.models import CustomUser
from account.serializers import Seri_users

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
@csrf_exempt
def list_mostgames(request):
    top_5_games = Games_Table.objects.order_by('-like')[:5]
    top_5_game_ids = top_5_games.values_list('id', flat=True)
    return JsonResponse(list(top_5_game_ids), safe=False)

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
            game.commentscount+=1
            game.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
@permission_classes([permissions.AllowAny])
@csrf_exempt
def list_gamegetlike(request):
    if request.method == 'GET':
        likes = Game_Like.objects.all()
        serializer = Seri_gameslike(likes, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
        except json.JSONDecodeError:
            return Response({'error': 'Invalid JSON'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = Seri_gameslike(data=data)
        if serializer.is_valid():
            user_id = serializer.validated_data['userID']
            game_id = serializer.validated_data['gameID']
            like = serializer.validated_data['like']
            dislike = serializer.validated_data['dislike']
            
            user = get_object_or_404(CustomUser, id=user_id)
            game = get_object_or_404(Games_Table, id=game_id)
            
            existing_like = Game_Like.objects.filter(userID=user_id, gameID=game_id).first()
            
            if existing_like:
                # Update existing like/dislike
                if existing_like.like and not like:
                    user.like_games -= 1
                    game.like -= 1
                if existing_like.dislike and not dislike:
                    game.dislike -= 1
                if not existing_like.like and like:
                    user.like_games += 1
                    game.like += 1
                if not existing_like.dislike and dislike:
                    game.dislike += 1
                
                existing_like.like = like
                existing_like.dislike = dislike
                existing_like.save()
                game.save()
                user.save()
                
                return JsonResponse({
                    "userID": str(user_id),
                    "gameID": str(game_id),
                    "like": like,
                    "dislike": dislike,
                    "likecount": game.like,
                    "dislikecount": game.dislike,
                    "usermov": user.like_game
                }, status=status.HTTP_200_OK)
            

            game_like = serializer.save()
            
            if game_like.like:
                user.like_games += 1
                game.like += 1
            if game_like.dislike:
                game.dislike += 1
            
            game.save()
            user.save()
            
            return JsonResponse({
                "userID": str(user_id),
                "gameID": str(game_id),
                "like": like,
                "dislike": dislike,
                "likecount": game.like,
                "dislikecount": game.dislike,
                "usermov": user.like_games
            }, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@csrf_exempt
def list_getidcomments(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            game_id = data.get('gameID')

            if game_id is not None:
                comments = Game_Comment.objects.filter(gameID=game_id)
                comment_serializer = Seri_gamescomment(comments, many=True)

                if comments.exists():
                    # Yorumların içine kullanıcı bilgilerini birleştir
                    comments_with_user_info = []
                    for comment in comments:
                        user = get_object_or_404(CustomUser, id=comment.userID)
                        comment_data = {
                            'id': comment.id,
                            'userID': comment.userID,
                            'movieID': comment.gameID,
                            'comment': comment.comment,
                            'savedate': comment.savedate,
                            'full_name': user.full_name,
                            'username': user.username,
                            'profil_picture': user.profil_picture.url if user.profil_picture else None
                        }
                        comments_with_user_info.append(comment_data)


                    return JsonResponse(comments_with_user_info, safe=False)
                else:
                    return JsonResponse({'message': 'No comments found for the provided game ID.'}, status=404)
            else:
                return JsonResponse({'message': 'No game ID provided.'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'message': 'Invalid JSON.'}, status=400)
    else:
        return JsonResponse({'message': 'Only POST requests are allowed.'}, status=405)
    
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
            return JsonResponse({'message': 'No game ID provided.'}, status=400)
    else:
        return JsonResponse({'message': 'Only POST requests are allowed.'}, status=405)

@csrf_exempt
def list_getidlikeusers(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        user_id = data.get('userID')
        if user_id is not None:  
            likes = Game_Like.objects.filter(userID=user_id,like=True)
            serializer = Seri_gameslike(likes, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse({'message': 'No user ID provided.'}, status=400)
    else:
        return JsonResponse({'message': 'Only POST requests are allowed.'}, status=405)
    
@csrf_exempt
def list_liked(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            game_id = data.get('userID')

            if game_id is not None:
                # gameID ile ilgili yorumları çek
                likes = Game_Like.objects.filter(userID=game_id,like=True)
                like_serializer = Seri_gameslike(likes, many=True)

                if likes.exists():
                    # Yorumların içine kullanıcı bilgilerini birleştir
                    likes_with_user_info = []
                    for like in likes:
                        game = get_object_or_404(Games_Table, id=like.gameID)
                        like_data = {
                            'id': like.id,
                            'userID': like.userID,
                            'gameID': like.gameID,
                            'like':like.like,
                            'dislike':like.dislike,
                            'savedate': like.savedate,
                            'name': game.name,
                            'urlname': game.urlname,
                            'production': game.production,
                            'about':game.about,
                            'release':game.release,
                            'background':game.background,
                            'poster':game.poster,
                            'like':game.like,
                            'dislike':game.dislike,
                            'commentcount':game.commentscount
                        }
                        likes_with_user_info.append(like_data)


                    return JsonResponse(likes_with_user_info, safe=False)
                else:
                    return JsonResponse({'message': 'No comments found for the provided game ID.'}, status=404)
            else:
                return JsonResponse({'message': 'No game ID provided.'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'message': 'Invalid JSON.'}, status=400)
    else:
        return JsonResponse({'message': 'Only POST requests are allowed.'}, status=405)
    
@csrf_exempt
def list_getcategory(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            catalog_id = data.get('catalogID')
            if catalog_id is not None:
                games = Games_Table.objects.filter(categories__id=catalog_id)
                games_data = []
                for game in games:
                    categories = [category.name for category in game.categories.all()]
                    game_data = {
                        'id': game.id,
                        'title': game.name,
                        'urlname': game.urlname,
                        'production': game.production,
                        'about': game.about,
                        'categories': categories,
                        'release': game.release.strftime('%Y-%m-%d'),
                        'background': game.background,
                        'poster': game.poster,
                        'savedate': game.savedate.strftime('%Y-%m-%d %H:%M:%S'),
                        'isPublished': game.isPublished,
                        'like': game.like,
                        'dislike': game.dislike,
                        'commentscount': game.commentscount
                    }
                    games_data.append(game_data)
                return JsonResponse(games_data, safe=False)
            else:
                return JsonResponse({'error': 'Catalog ID is required'}, status=400)
        except json.decoder.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)
        except ValueError:
            return JsonResponse({'error': 'Invalid catalog ID'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)
    
@csrf_exempt
def delete_comment(request):
    if request.method=='POST':
        data = json.loads(request.body)
        comment_id = data.get('commentID')
        try:
            Game_Comment.objects.filter(id=comment_id).delete()
            return JsonResponse({'message':'Comment deleting successfully'})
        except (Game_Comment.DoesNotExist):
            return JsonResponse({'message': 'Comment not found'}, status=404)
    else:
        return JsonResponse({'message': 'POST is important'}, status=405)