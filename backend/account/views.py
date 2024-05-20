import json
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import CustomUser

@csrf_exempt
def get_all_users(request):
    users = CustomUser.objects.all()
    user_data = [{'id': user.id, 'full_name': user.full_name, 'email': user.email} for user in users]
    return JsonResponse({'users': user_data})

@csrf_exempt
def get_user_info(request):
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
                    'x_link': user.x_link,
                    'instagram_link': user.instagram_link,
                    'facebook_link': user.facebook_link,
                    'linkedin_link': user.linkedin_link
                }
                return JsonResponse({'user': user_data})
            except CustomUser.DoesNotExist:
                return JsonResponse({'error': 'User does not exist'}, status=404)
        else:
            return JsonResponse({'error': 'User ID is required'}, status=400)
    else:
        return JsonResponse({'error': 'POST method is required'}, status=405)

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
                profil_picture=data.get('profile_picture'),
                x_link = data.get('x_link')
                instagram_link = data.get('instagram_link')
                facebook_link = data.get('facebook_link')
                linkedin_link = data.get('linkedin_link')

                user.full_name = full_name
                user.email = email
                user.username = username
                user.profil_picture=profil_picture
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
                'profil_picture':user.profile_picture,
                'x_link': user.x_link,
                'instagram_link': user.instagram_link,
                'facebook_link': user.facebook_link,
                'linkedin_link': user.linkedin_link,
                'savedate':user.savedate
                }

                return JsonResponse({'success': 'User information updated successfully','user': user_data})
            except CustomUser.DoesNotExist:
                return JsonResponse({'error': 'User does not exist'}, status=404)
        else:
            return JsonResponse({'error': 'User ID is required'}, status=400)
    else:
        return JsonResponse({'error': 'POST method is required'}, status=405)

@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            user_data = {
                'id': user.id,
                'full_name': user.full_name,
                'email': user.email,
                'username': user.username,
                'profil_picture':user.profile_picture,
                'x_link': user.x_link,
                'instagram_link': user.instagram_link,
                'facebook_link': user.facebook_link,
                'linkedin_link': user.linkedin_link,
                'savedate': user.savedate
            }
            return JsonResponse({'success': 'Login successful', 'user': user_data})
        else:
            return JsonResponse({'error': 'Invalid email or password'}, status=401)
    else:
        return JsonResponse({'error': 'POST method is required'}, status=405)


@csrf_exempt    
def user_register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        full_name = data.get('full_name')
        email = data.get('email')
        password = data.get('password')

        if not (full_name and email and password):
            return JsonResponse({'error': 'Full name, email, and password are required'}, status=400)

        # CustomUser modelini kullanarak yeni bir kullanıcı oluştur
        user = CustomUser.objects.create_user(username=email, email=email, password=password)
        user.full_name = full_name
        user.save()
        user_data = {
            'id': user.id,
            'full_name': user.full_name,
            'email': user.email,
            'username': user.username,
            'profil_picture':user.profile_picture,
            'x_link': user.x_link,
            'instagram_link': user.instagram_link,
            'facebook_link': user.facebook_link,
            'linkedin_link': user.linkedin_link,
            'savedate':user.savedate
        }

        return JsonResponse({'success': 'User registered successfully', 'user': user_data})
    else:
        return JsonResponse({'error': 'POST method is required'}, status=405)


@csrf_exempt
def user_logout(request):
    if request.method == 'POST':
        logout(request)
        return JsonResponse({'success': 'Logout successful'})
    else:
        return JsonResponse({'error': 'POST method is required'}, status=405)
