from django.shortcuts import get_object_or_404
from rest_framework import permissions,status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from .models import Book_Table,Book_Category,Book_Like,Book_Comment
from .serializers import Seri_booktable,Seri_bookcategory,Seri_bookcomment,Seri_booklike
from django.views.decorators.csrf import csrf_exempt
import json,uuid
from django.http import JsonResponse
from account.models import CustomUser
from account.serializers import Seri_users

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
@csrf_exempt
def list_mostbooks(request):
    top_5_book = Book_Table.objects.order_by('-like')[:5]
    top_5_book_ids = top_5_book.values_list('id', flat=True)
    return JsonResponse(list(top_5_book_ids), safe=False)


#obj= tüm objectleri tutar
#seri=obj response için seriliazer uygular

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
@csrf_exempt
def list_bookcategory(request):
    obj=Book_Category.objects.all()
    seri=Seri_bookcategory(obj,many=True)
    return Response(seri.data)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
@csrf_exempt
def list_booktable(request):
    obj=Book_Table.objects.all()
    seri=Seri_booktable(obj,many=True)
    return Response(seri.data)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
@csrf_exempt
def list_bookcategoryid(request,id):
    obj=get_object_or_404(Book_Category,id=id)
    seri=Seri_bookcategory(obj)
    return Response(seri.data)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
@csrf_exempt
def list_bookcomment(request):
    obj=Book_Comment.objects.all()
    seri=Seri_bookcomment(obj,many=True)
    return Response(seri.data)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
@csrf_exempt
def list_booklike(request):
    obj=Book_Like.objects.all()
    seri=Seri_booklike(obj,many=True)
    return Response(seri.data)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
@csrf_exempt
def list_bookid(request,id):
    obj=get_object_or_404(Book_Table,id=id)
    seri=Seri_booktable(obj)
    return Response(seri.data)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
@csrf_exempt
def list_bookurlname(request,urlname):
    obj=get_object_or_404(Book_Table,urlname=urlname)
    seri=Seri_booktable(obj)
    return Response(seri.data)

@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
@csrf_exempt
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
            book.commentscount+=1
            book.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def list_bookgetlike(request):
    if request.method == 'GET':
        likes = Book_Like.objects.all()
        serializer = Seri_booklike(likes, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
        except json.JSONDecodeError:
            return Response({'message': 'Invalid JSON'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = Seri_booklike(data=data)
        if serializer.is_valid():
            user_id = serializer.validated_data['userID']
            book_id = serializer.validated_data['bookID']
            like = serializer.validated_data['like']
            dislike = serializer.validated_data['dislike']
            
            user = get_object_or_404(CustomUser, id=user_id)
            book = get_object_or_404(Book_Table, id=book_id)
            
            existing_like = Book_Like.objects.filter(userID=user_id, bookID=book_id).first()
            
            if existing_like:
                # Update existing like/dislike
                if existing_like.like and not like:
                    user.like_book -= 1
                    book.like -= 1
                if existing_like.dislike and not dislike:
                    book.dislike -= 1
                if not existing_like.like and like:
                    user.like_book += 1
                    book.like += 1
                if not existing_like.dislike and dislike:
                    book.dislike += 1
                
                existing_like.like = like
                existing_like.dislike = dislike
                existing_like.save()
                book.save()
                user.save()
                
                return JsonResponse({
                    "userID": str(user_id),
                    "bookID": str(book_id),
                    "like": like,
                    "dislike": dislike,
                    "likecount": book.like,
                    "dislikecount": book.dislike,
                    "usermov": user.like_book
                }, status=status.HTTP_200_OK)
            

            book_like = serializer.save()
            
            if book_like.like:
                user.like_book += 1
                book.like += 1
            if book_like.dislike:
                book.dislike += 1
            
            book.save()
            user.save()
            
            return JsonResponse({
                "userID": str(user_id),
                "bookID": str(book_id),
                "like": like,
                "dislike": dislike,
                "likecount": book.like,
                "dislikecount": book.dislike,
                "usermov": user.like_book
            }, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@csrf_exempt
def list_getidcomments(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            book_id = data.get('bookID')

            if book_id is not None:
                comments = Book_Comment.objects.filter(bookID=book_id)
                comment_serializer = Seri_bookcomment(comments, many=True)

                if comments.exists():
                    comments_with_user_info = []
                    for comment in comments:
                        user = get_object_or_404(CustomUser, id=comment.userID)
                        comment_data = {
                            'id': comment.id,
                            'userID': comment.userID,
                            'bookID': comment.bookID,
                            'comment': comment.comment,
                            'savedate': comment.savedate,
                            'full_name': user.full_name,
                            'username': user.username,
                            'profil_picture': user.profil_picture.url if user.profil_picture else None
                        }
                        comments_with_user_info.append(comment_data)


                    return JsonResponse(comments_with_user_info, safe=False)
                else:
                    return JsonResponse({'message': 'No comments found for the provided book ID.'}, status=404)
            else:
                return JsonResponse({'message': 'No book ID provided.'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'message': 'Invalid JSON.'}, status=400)
    else:
        return JsonResponse({'message': 'Only POST requests are allowed.'}, status=405)
    
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
            return JsonResponse({'message': 'No book ID provided.'}, status=400)
    else:
        return JsonResponse({'message': 'Only POST requests are allowed.'}, status=405)

@csrf_exempt
def list_getidlikeusers(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        user_id = data.get('userID')
        if user_id is not None:  
            likes = Book_Like.objects.filter(userID=user_id,like=True)
            serializer = Seri_booklike(likes, many=True)
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
            book_id = data.get('userID')

            if book_id is not None:
                likes = Book_Like.objects.filter(userID=book_id,like=True)
                like_serializer = Seri_booklike(likes, many=True)

                if likes.exists():
                    likes_with_user_info = []
                    for like in likes:
                        book = get_object_or_404(Book_Table, id=like.bookID)
                        like_data = {
                            'id': like.id,
                            'userID': like.userID,
                            'bookID': like.bookID,
                            'like':like.like,
                            'dislike':like.dislike,
                            'savedate': like.savedate,
                            'name': book.name,
                            'urlname': book.urlname,
                            'production': book.production,
                            'about':book.about,
                            'release':book.release,
                            'background':book.background,
                            'poster':book.poster,
                            'like':book.like,
                            'dislike':book.dislike,
                            'commentcount':book.commentscount
                        }
                        likes_with_user_info.append(like_data)


                    return JsonResponse(likes_with_user_info, safe=False)
                else:
                    return JsonResponse({'message': 'No comments found for the provided book ID.'}, status=404)
            else:
                return JsonResponse({'message': 'No book ID provided.'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'message': 'Invalid JSON.'}, status=400)
    else:
        return JsonResponse({'message': 'Only POST requests are allowed.'}, status=405)
    
def list_getcategory(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            catalog_id = data.get('catalogID')
            if catalog_id is not None:
                books = Book_Table.objects.filter(categories__id=catalog_id)
                books_data = []
                for book in books:
                    categories = [category.name for category in book.categories.all()]
                    book_data = {
                        'id': book.id,
                        'title': book.name,
                        'urlname': book.urlname,
                        'production': book.production,
                        'about': book.about,
                        'categories': categories,
                        'release': book.release.strftime('%Y-%m-%d'),
                        'background': book.background,
                        'poster': book.poster,
                        'savedate': book.savedate.strftime('%Y-%m-%d %H:%M:%S'),
                        'isPublished': book.isPublished,
                        'like': book.like,
                        'dislike': book.dislike,
                        'commentscount': book.commentscount
                    }
                    books_data.append(book_data)
                return JsonResponse(books_data, safe=False)
            else:
                return JsonResponse({'error': 'Catalog ID is required'}, status=400)
        except json.decoder.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)
        except ValueError:
            return JsonResponse({'error': 'Invalid catalog ID'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)
