from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions,status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from .models import Movies_Table,Movies_Comment,Movies_Category,Movies_Like
from .serializers import Seri_movietable,Seri_moviecategory,Seri_moviecomment,Seri_movielike
import json


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
@csrf_exempt
def list_movie(request):
    obj=Movies_Table.objects.all()
    seri=Seri_movietable(obj,many=True)
    return Response(seri.data)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
@csrf_exempt
def list_moviecategory(request):
    obj=Movies_Category.objects.all()
    seri=Seri_moviecategory(obj,many=True)
    return Response(seri.data)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
@csrf_exempt
def list_moviecomment(request):
    obj=Movies_Comment.objects.all()
    seri=Seri_moviecomment(obj,many=True)
    return Response(seri.data)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
@csrf_exempt
def list_movielike(request):
    obj=Movies_Like.objects.all()
    seri=Seri_movielike(obj,many=True)
    return Response(seri.data)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
@csrf_exempt
def list_movieid(request,id):
    obj=get_object_or_404(Movies_Table,id=id)
    seri=Seri_movietable(obj)
    return Response(seri.data)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
@csrf_exempt
def list_moviecategoryid(request,id):
    obj=get_object_or_404(Movies_Category,id=id)
    seri=Seri_moviecategory(obj)
    return Response(seri.data)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
@csrf_exempt
def list_movieurlname(request,urlname):
    obj=get_object_or_404(Movies_Table,urlname=urlname)
    seri=Seri_movietable(obj)
    return Response(seri.data)



@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
@csrf_exempt
def list_moviegetcomment(request):
    if request.method == 'GET':
        comments = Movies_Comment.objects.all()
        serializer = Seri_moviecomment(comments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        serializer = Seri_moviecomment(data=data)
        if serializer.is_valid():
            movie_comment=serializer.save()
            movie = get_object_or_404(Movies_Table, id=movie_comment.movieID)
            if movie_comment.commentscount:
                movie.commentscount+= 1
            movie.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
@permission_classes([permissions.AllowAny])
def list_moviegetlike(request):
    if request.method == 'GET':
        likes = Movies_Like.objects.all()
        serializer = Seri_movielike(likes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        serializer = Seri_movielike(data=data)
        if serializer.is_valid():
            user_id = serializer.validated_data['userID']
            movie_id = serializer.validated_data['movieID']
            like = serializer.validated_data['like']
            dislike = serializer.validated_data['dislike']
            existing_like = Movies_Like.objects.filter(userID=user_id, movie_id=movie_id).first()
            
            if existing_like:
                if existing_like.like and not like:
                    existing_like.movieID.like -= 1
                if existing_like.dislike and not dislike:
                    existing_like.movieID.dislike -= 1
                if not existing_like.like and like:
                    existing_like.movieID.like += 1
                if not existing_like.dislike and dislike:
                    existing_like.movieID.dislike += 1
                existing_like.like = like
                existing_like.dislike = dislike
                existing_like.save()
                existing_like.movieID.save()
                
                return JsonResponse({"data": serializer.data, "like": existing_like.movieID.like, "dislike": existing_like.movieID.dislike}, status=status.HTTP_200_OK)
            movie_like = serializer.save()
            movie = get_object_or_404(Movies_Table, id=movie_id)
            if movie_like.like:
                movie.like += 1
            if movie_like.dislike:
                movie.dislike += 1
            movie.save()
            
            return JsonResponse({"data": serializer.data, "like": movie.like, "dislike": movie.dislike}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@csrf_exempt
def list_getidcomments(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        movie_id = data.get('movieID')
        if movie_id is not None:  
            comments = Movies_Comment.objects.filter(movieID=movie_id)
            serializer = Seri_moviecomment(comments, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse({'error': 'No movie ID provided.'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed.'}, status=405)
    
@csrf_exempt
def list_getidlikes(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        movie_id = data.get('movieID')
        if movie_id is not None:  
            comments = Movies_Like.objects.filter(movieID=movie_id)
            serializer = Seri_movielike(comments, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse({'error': 'No movie ID provided.'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed.'}, status=405)
    
def list_getidlikeusers(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        user_id = data.get('userID')
        if user_id is not None:  
            likes = Movies_Like.objects.filter(user_id=user_id)
            serializer = Seri_movielike(likes, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse({'error': 'No user ID provided.'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed.'}, status=405)
    
