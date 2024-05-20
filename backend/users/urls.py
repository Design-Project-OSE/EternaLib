from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register_user, name='register'),
    path('login', views.user_login, name='user_login'),
    path('profile/<uuid:pk>', views.UserProfileAPIView.as_view(), name='Kullanıcı Profili alma GET'),
    path('profile/edit', views.UserProfileUpdateAPIView.as_view, name='Kullanıcı Profili düzenleme POST'),
    path('forgorpass',views.forgot_password,name="Şifre Unutma"),

]