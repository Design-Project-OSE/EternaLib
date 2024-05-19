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


@csrf_exempt
def register_user(request):
    if request.method == 'POST':
        try:
            # Angular'dan gelen verileri al
            namesurname = request.POST.get('namesurname').replace(' ', '_')
            email = request.POST.get('email')
            password = request.POST.get('password')
            
            # Django kullanıcı nesnesini oluştur
            user = User.objects.create_user(username=namesurname, email=email, password=password)
            
            # Ekstra bilgileri kaydetmek istiyorsanız CustomUser modelini kullanabilirsiniz
            # custom_user = CustomUser.objects.create(user=user, isim_soyisim=namesurname)

            # Başarılı yanıtı döndür
            return JsonResponse({'message': 'Kullanıcı başarıyla oluşturuldu.'}, status=201)
        except Exception as e:
            # Hata durumunda yanıtı döndür
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Yanlış istek methodu.'}, status=405)
    


@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Kullanıcıyı doğrula
        user = authenticate(username=email, password=password)

        if user:
            # Kullanıcı doğrulandıysa, bir token oluştur ve geri döndür
            token, _ = Token.objects.get_or_create(user=user)
            return JsonResponse({'token': token.key})
        else:
            # Kullanıcı doğrulanamadıysa hata mesajı döndür
            return JsonResponse({'error': 'Geçersiz e-posta veya şifre'}, status=400)

    else:
        return JsonResponse({'error': 'Sadece POST istekleri kabul edilir'}, status=405)
    


class UserProfileAPIView(generics.RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    
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
            return Response({'success': 'Profil başarıyla güncellendi'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        # Kullanıcı e-postasına sahip olan bir kullanıcıyı getir
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Bu e-posta adresine sahip bir kullanıcı bulunamadı.'})

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

        return JsonResponse({'status': 'success', 'message': 'Yeni şifreniz e-posta adresinize gönderilmiştir.'})

    return JsonResponse({'status': 'error', 'message': 'Geçersiz istek methodu.'})

def user_logout(request):
    logout(request)
    return redirect('anasayfa')