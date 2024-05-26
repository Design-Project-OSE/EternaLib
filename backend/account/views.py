import json
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import CustomUser
from rest_framework.authtoken.models import Token
from django.db import IntegrityError
from django.core.files.storage import FileSystemStorage
import random,uuid
from movies.models import Movies_Comment,Movies_Like,Movies_Table
from game.models import Game_Comment,Game_Like,Games_Table
from book.models import Book_Comment,Book_Like,Book_Table

@csrf_exempt
def get_all_users(request):
    users = CustomUser.objects.all()
    user_data = [{'id': user.id,
                    'full_name': user.full_name,
                    'email': user.email,
                    'username': user.username,
                    'password':user.password,
                    'about':user.about,
                    'profil_picture': user.profil_picture.url if user.profil_picture else None,
                    'x_link': user.x_link,
                    'instagram_link': user.instagram_link,
                    'facebook_link': user.facebook_link,
                    'linkedin_link': user.linkedin_link,
                    'like_movie':user.like_movie,
                    'like_games':user.like_games,
                    'like_book':user.like_book
                    } for user in users]
    return JsonResponse({'users':user_data})

@csrf_exempt
def get_userid_info(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        userID = data.get('userID')
        if userID:
            try:
                user = CustomUser.objects.get(id=userID)
                user_data = {
                    'id': user.id,
                    'full_name': user.full_name,
                    'email': user.email,
                    'username': user.username,
                    'password':user.password,
                    'about':user.about,
                    'profil_picture': user.profil_picture.url if user.profil_picture else None,
                    'x_link': user.x_link,
                    'instagram_link': user.instagram_link,
                    'facebook_link': user.facebook_link,
                    'linkedin_link': user.linkedin_link,
                    'like_movie':user.like_movie,
                    'like_games':user.like_games,
                    'like_book':user.like_book
                }
                return JsonResponse({**user_data})
            except CustomUser.DoesNotExist:
                return JsonResponse({'message': 'User does not exist'}, status=404)
        else:
            return JsonResponse({'message': 'User ID is required'}, status=400)
    else:
        return JsonResponse({'message': 'POST method is required'}, status=405)
    
@csrf_exempt
def get_username_info(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        if username:
            try:
                user = CustomUser.objects.get(username=username)
                user_data = {
                    'id': user.id,
                    'full_name': user.full_name,
                    'email': user.email,
                    'username': user.username,
                    'password':user.password,
                    'about':user.about,
                    'profil_picture': user.profil_picture.url if user.profil_picture else None,
                    'x_link': user.x_link,
                    'instagram_link': user.instagram_link,
                    'facebook_link': user.facebook_link,
                    'linkedin_link': user.linkedin_link,
                    'like_movie':user.like_movie,
                    'like_games':user.like_games,
                    'like_book':user.like_book
                }
                return JsonResponse({**user_data})
            except CustomUser.DoesNotExist:
                return JsonResponse({'message': 'User does not exist'}, status=404)
        else:
            return JsonResponse({'message': 'User ID is required'}, status=400)
    else:
        return JsonResponse({'message': 'POST method is required'}, status=405)

@csrf_exempt
def update_user_info(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        userID = data.get('userID')
        if userID:
            try:
                user = CustomUser.objects.get(id=userID)
                full_name = data.get('full_name')
                email = data.get('email')
                username = data.get('username')
                about=data.get('about')
                profil_picture = data.get('profil_picture')
                x_link = data.get('x_link')
                instagram_link = data.get('instagram_link')
                facebook_link = data.get('facebook_link')
                linkedin_link = data.get('linkedin_link')
                if 'profil_picture' in request.FILES:
                    profil_picture = request.FILES['profil_picture']
                    fs = FileSystemStorage(location='backend/images')
                    filename = fs.save(profil_picture.name, profil_picture)
                    uploaded_file_url = fs.url(filename)
                    user.profil_picture = filename 

                user.full_name = full_name
                user.email = email
                user.username = username
                user.about=about
                user.profil_picture = profil_picture
                user.x_link = x_link
                user.instagram_link = instagram_link
                user.facebook_link = facebook_link
                user.linkedin_link = linkedin_link
                user.save()
                user_data = {
                    'id': user.id,
                    'full_name': user.full_name,
                    'email': user.email,
                    'username': user.username,
                    'about':user.about,
                    'profil_picture': user.profil_picture.url if user.profil_picture else None,
                    'x_link': user.x_link,
                    'instagram_link': user.instagram_link,
                    'facebook_link': user.facebook_link,
                    'linkedin_link': user.linkedin_link,
                    'savedate': user.savedate
                }

                return JsonResponse({'message': 'User information updated messagefully', **user_data})
            except CustomUser.DoesNotExist:
                return JsonResponse({'message': 'User does not exist'}, status=404)
        else:
            return JsonResponse({'message': 'User ID is required'}, status=400)
    else:
        return JsonResponse({'message': 'POST method is required'}, status=405)

@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            try:
                token = Token.objects.create(user=user)
            except IntegrityError:
                token = Token.objects.get(user=user)
            login(request, user)
            user_data = {
                'id': user.id,
                'full_name': user.full_name,
                'email': user.email,
                'username': user.username,
                'password':user.password,
            }
            return JsonResponse({'message': 'Login messageful', 'token': token.key, **user_data})
        else:
            return JsonResponse({'message': 'Invalid email or password'}, status=401)
    else:
        return JsonResponse({'message': 'POST method is required'}, status=405)

@csrf_exempt
def user_register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        full_name = data.get('full_name')
        email = data.get('email')
        password = data.get('password')

        if not (full_name and email and password):
            return JsonResponse({'message': 'Full name, email, and password are required'}, status=400)

        if CustomUser.objects.filter(email=email).exists():
            return JsonResponse({'message': 'Email is already in use'}, status=400)

        user = CustomUser.objects.create_user(username=email, email=email, password=password)
        user.full_name = full_name
        username = full_name.lower().replace(' ', '_').replace('ş', 's').replace('ğ', 'g').replace('ç', 'c').replace('ı', 'i').replace('ö', 'o').replace('ü', 'u')
        sp_ch=''.join([str(random.randint(0, 9)) for _ in range(4)])
        user.username=username+sp_ch
        user.save()
        try:
            token = Token.objects.create(user=user)
        except IntegrityError:
            token = Token.objects.get(user=user)

        user_data = {
            'id': user.id,
            'full_name': user.full_name,
            'email': user.email,
            'username': user.username,
            'profil_picture': user.profil_picture.url if user.profil_picture else None,
            'x_link': user.x_link,
            'instagram_link': user.instagram_link,
            'facebook_link': user.facebook_link,
            'linkedin_link': user.linkedin_link,
            'savedate': user.savedate,
            'like_movie': user.like_movie,
            'like_games': user.like_games,
            'like_book': user.like_book
        }

        return JsonResponse({'message': 'User registered messagefully', 'token': token.key, **user_data})
    else:
        return JsonResponse({'message': 'POST method is required'}, status=405)

@csrf_exempt
def user_logout(request):
    if request.method == 'POST':
        logout(request)
        return JsonResponse({'message': 'Logout messageful'})
    else:
        return JsonResponse({'message': 'POST method is required'}, status=405)
    
@csrf_exempt
def delete_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'message': 'Invalid JSON'}, status=400)

        userID = data.get('userID')
        if userID:
            try:
                user = CustomUser.objects.get(id=userID)
                Movies_Comment.objects.filter(userID=userID).delete()
                Game_Comment.objects.filter(userID=userID).delete()
                Book_Comment.objects.filter(userID=userID).delete()
                Book_Like.objects.filter(userID=userID).delete()
                Movies_Like.objects.filter(userID=userID).delete()
                Game_Like.objects.filter(userID=userID).delete()
                user.delete()

                movcomlen = Movies_Comment.objects.count()
                movlikelen = Movies_Like.objects.filter(like=True).count()
                movdislikelen = Movies_Like.objects.filter(dislike=True).count()

                Movies_Table.commentscount = movcomlen
                Movies_Table.like = movlikelen
                Movies_Table.dislike = movdislikelen
                Movies_Table.save()

                gamelen = Game_Comment.objects.count()
                gamelikelen = Game_Like.objects.filter(like=True).count()
                gamedislikelen = Game_Like.objects.filter(dislike=True).count()

                Games_Table.commentscount = gamelen
                Games_Table.like = gamelikelen
                Games_Table.dislike = gamedislikelen
                Games_Table.save()

                booklen = Book_Comment.objects.count()
                booklikelen = Book_Like.objects.filter(like=True).count()
                bookdislikelen = Book_Like.objects.filter(dislike=True).count()

                Book_Table.commentscount = booklen
                Book_Table.like = booklikelen
                Book_Table.dislike = bookdislikelen
                Book_Table.save()

                return JsonResponse({'message': 'Kullanıcı başarıyla silindi'})
            except CustomUser.DoesNotExist:
                return JsonResponse({'message': 'Kullanıcı mevcut değil'}, status=404)
        else:
            return JsonResponse({'message': 'Kullanıcı ID gerekli'}, status=400)
    else:
        return JsonResponse({'message': 'POST yöntemi gereklidir'}, status=405)
    
@csrf_exempt
def change_password(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_id = data.get('userID')
        current_password = data.get('current_password')
        new_password = data.get('new_password')

        try:
            user_id = uuid.UUID(user_id)
            user = CustomUser.objects.get(id=user_id)
        except (ValueError, CustomUser.DoesNotExist):
            return JsonResponse({'message': 'User not found'}, status=404)

        if not user.check_password(current_password):
            return JsonResponse({'message': 'Current password is wrong!'}, status=400)

        user.set_password(new_password)
        user.save()

        return JsonResponse({'message': 'Password changed successfully'})

    else:
        return JsonResponse({'message': 'POST is important'}, status=405)
    
@csrf_exempt
def update_profilpictures(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        userID = data.get('userID')
        if userID:
            try:
                user = CustomUser.objects.get(id=userID)
                profil_picture = data.get('profil_picture')
                if 'profil_picture' in request.FILES:
                    profil_picture = request.FILES['profil_picture']
                    fs = FileSystemStorage(location='backend/images')
                    filename = fs.save(profil_picture.name, profil_picture)
                    uploaded_file_url = fs.url(filename)
                    user.profil_picture = filename 


                user.profil_picture = profil_picture
                user.save()
                user_data = {
                    'id': user.id,
                    'profil_picture': user.profil_picture.url if user.profil_picture else None,
                    'url':uploaded_file_url
                }

                return JsonResponse({'message': 'User information updated messagefully', **user_data})
            except CustomUser.DoesNotExist:
                return JsonResponse({'message': 'User does not exist'}, status=404)
        else:
            return JsonResponse({'message': 'User ID is required'}, status=400)
    else:
        return JsonResponse({'message': 'POST method is required'}, status=405)