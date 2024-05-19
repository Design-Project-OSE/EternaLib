from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout
from rest_framework.authtoken.models import Token
from rest_framework import generics
from .models import UserProfile
from .serializers import UserProfileSerializer
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
import json
from rest_framework import generics

@csrf_exempt
def register_user(request):
    if request.method == 'POST':
        try:
            # Angular'dan gelen verileri al
            data=json.loads(request.body.decode('utf-8'))
            namesurname = data.get('namesurname').replace(' ', '_')
            email = data.get('email')
            password = data.get('password')
            
            User = get_user_model()
            # Django kullanıcı nesnesini oluştur
            user = User.objects.create_user(username=namesurname, email=email, password=password)
            
            # Ekstra bilgileri kaydetmek istiyorsanız CustomUser modelini kullanabilirsiniz
            # custom_user = CustomUser.objects.create(user=user, isim_soyisim=namesurname)

            # Başarılı yanıtı döndür
            return JsonResponse({'message': 'User created successfully.'}, status=201)
        except Exception as e:
            # Hata durumunda yanıtı döndür
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Wrong request method.'}, status=405)
    


@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        email = data.get('email')
        password = data.get('password')

        # Kullanıcıyı doğrula
        user = authenticate(username=email, password=password)

        if user:
            # Doğru bir şekilde UUID oluştur
            token = Token.objects.create(user=user)
            return JsonResponse({'token': token.key, 'user_id': user.id})
        else:
            # Kullanıcı doğrulanamadıysa hata mesajı döndür
            return JsonResponse({'error': 'Invalid email or password'}, status=400)

    else:
        return JsonResponse({'error': 'Only POST requests are accepted'}, status=405)
    


class UserProfileAPIView(generics.RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    lookup_field = 'pk'
    
class UserProfileUpdateAPIView(APIView):
    def put(self, request, *args, **kwargs):
        # Kullanıcı bilgilerini al
        user = request.user
        data = request.data

        # Kullanıcının profilini al veya oluştur
        profile, created = UserProfile.objects.get_or_create(user=user)

        # Serializer ile gelen verileri kontrol et
        serializer = UserProfileSerializer(instance=profile, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': 'Profile successfully updated'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        # Kullanıcı e-postasına sahip olan bir kullanıcıyı getir
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'No user with this e-mail address was found.'})

        # Yeni bir şifre oluştur ve kullanıcıya atayın
        new_password = User.objects.make_random_password()
        user.set_password(new_password)
        user.save()

        # Kullanıcıya yeni şifreyi içeren bir e-posta gönder
        send_mail(
            'Şifre Sıfırlama',
            f'Merhaba {user.username},\n\nYeni şifreniz: {new_password}\n\nLütfen giriş yaptıktan sonra şifrenizi değiştirin.',
            'eternalib@outlook.com',
            [email],
            fail_silently=False,
        )

        return JsonResponse({'status': 'success', 'message': 'Your new password has been sent to your e-mail address.'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})

def user_logout(request):
    logout(request)
    return redirect('anasayfa')