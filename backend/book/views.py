from django.shortcuts import get_object_or_404
from rest_framework import permissions,status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from .models import Book_Table,Book_Category,Book_Like,Book_Comment
from .serializers import Seri_booktable,Seri_bookcategory,Seri_bookcomment,Seri_booklike
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse

#obj= tüm objectleri tutar
#seri=obj response için seriliazer uygular

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def list_bookcategory(request):
    obj=Book_Category.objects.all()
    seri=Seri_bookcategory(obj,many=True)
    return Response(seri.data)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def list_booktable(request):
    obj=Book_Table.objects.all()
    seri=Seri_booktable(obj,many=True)
    return Response(seri.data)
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def list_bookcategoryid(request,id):
    obj=get_object_or_404(Book_Category,id=id)
    seri=Seri_bookcategory(obj)
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

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def list_bookid(request,id):
    obj=get_object_or_404(Book_Table,id=id)
    seri=Seri_booktable(obj)
    return Response(seri.data)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def list_bookurlname(request,urlname):
    obj=get_object_or_404(Book_Table,urlname=urlname)
    seri=Seri_booktable(obj)
    return Response(seri.data)

@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def list_bookgetcomment(request):
    if request.method == 'GET':
        comments = Book_Comment.objects.all()
        serializer = Seri_bookcomment(comments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = Seri_bookcomment(data=request.data)
        if serializer.is_valid():
            book_comment=serializer.save()
            book = get_object_or_404(Book_Table, id=book_comment.bookID)
            if book_comment.commentscount:
                book.commentscount+=1
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
@permission_classes([permissions.AllowAny])
def list_bookgetlike(request):
    if request.method == 'GET':
        likes = Book_Like.objects.all()
        serializer = Seri_booklike(likes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        serializer = Seri_booklike(data=data)
        if serializer.is_valid():
            user_id = serializer.validated_data['userID']
            book_id = serializer.validated_data['bookID']
            book = get_object_or_404(Book_Table, id=book_id)
            like = serializer.validated_data['like']
            dislike = serializer.validated_data['dislike']
            existing_like = Book_Like.objects.filter(userID=user_id, bookID=book_id).first()
            
            if existing_like:
                book = get_object_or_404(Book_Table, id=book_id)
                if existing_like.like and not like:
                    book.like -= 1
                if existing_like.dislike and not dislike:
                    book.dislike -= 1
                if not existing_like.like and like:
                    book.like += 1
                if not existing_like.dislike and dislike:
                    book.dislike += 1
                existing_like.like = like
                existing_like.dislike = dislike
                existing_like.save()
                book.save()
                
                return JsonResponse({**data,  "likecount": book.like, "dislikecount": book.dislike,'like':like,'dislike':dislike}, status=status.HTTP_200_OK)

            book_like = serializer.save()
            
            if book_like.like:
                book.like += 1
            if book_like.dislike:
                book.dislike += 1
            book.save()
            
            return JsonResponse({**data, "likecount": book.like, "dislikecount": book.dislike,'like':like,'dislike':dislike}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@csrf_exempt
def list_getidcomments(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        book_id = data.get('bookID')
        if book_id is not None:  
            comments = Book_Comment.objects.filter(bookID=book_id)
            serializer = Seri_bookcomment(comments, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse({'error': 'No book ID provided.'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed.'}, status=405)
    
@csrf_exempt
def list_getidlikes(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        book_id = data.get('bookID')
        if book_id is not None:  
            comments = Book_Like.objects.filter(bookID=book_id)
            serializer = Seri_booklike(comments, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse({'error': 'No book ID provided.'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed.'}, status=405)
    
def list_getidlikeusers(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        user_id = data.get('userID')
        if user_id is not None:  
            likes = Book_Like.objects.filter(user_id=user_id)
            serializer = Seri_booklike(likes, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse({'error': 'No user ID provided.'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed.'}, status=405)
    
