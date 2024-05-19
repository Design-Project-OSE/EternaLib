from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('api/login/', views.user_login, name='user_login'),
    path('api/profile/', views.UserProfileAPIView.as_view(), name='user-profile-api'),
    path('api/forgorpass/',views.forgot_password,name="Şifre Unutma"),
    path('logout/', views.user_logout, name='logout'),
]