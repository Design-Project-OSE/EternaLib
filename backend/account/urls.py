from django.urls import path
from . import views

urlpatterns = [
    path('accounts', views.get_all_users, name='[GET] ETKİ=[tüm kullanıcılar] INPUTS=[]'),
    path('account', views.get_user_info, name='[POST] ETKİ=[userID verisi verilen kullanıcının bilgileri] INPUTS=[userID]'),
    path('account/update', views.update_user_info, name='[POST] ETKİ=[userID verilen kullanıcı verilerini günceller] INPUTS=[userID,fullname,email,username,x_link,instagram_link,facebook_link,linkedin_link]'),
    path('login',views.user_login,name="[POST] ETKİ=[Giriş yapar] INPUTS=[email,password]"),
    path('register',views.user_register,name="[POST] ETKİ=[Kayıt İşlemi] INPUTS=[full_name,email,password]"),
    path('logout',views.user_logout,name="[GET] ETKİ=[Çıkış] INPUTS=[]"),
]
