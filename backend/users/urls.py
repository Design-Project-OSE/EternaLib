from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('api/login/', views.user_login, name='user_login'),
    path('api/profile/<uuid:pk>', views.UserProfileAPIView.as_view(), name='Kullanıcı Profili alma GET'),
    path('api/profile/edit', views.UserProfileUpdateAPIView.as_view, name='Kullanıcı Profili düzenleme POST'),
    path('api/forgorpass/',views.forgot_password,name="Şifre Unutma"),
    path('logout/', views.user_logout, name='logout'),
]