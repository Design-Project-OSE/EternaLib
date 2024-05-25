from django.urls import path
from . import views

urlpatterns = [
    path('accounts', views.get_all_users, name='[GET] ETKİ=[tüm kullanıcılar] INPUTS=[]'),
    path('account', views.get_userid_info, name='[POST] ETKİ=[userID verisi verilen kullanıcının bilgileri] INPUTS=[userID]'),
    path('account/username', views.get_username_info, name='[POST] ETKİ=[username verisi verilen kullanıcının bilgileri] INPUTS=[username]'),
    path('account/update', views.update_user_info, name='[POST] ETKİ=[userID verilen kullanıcı verilerini günceller] INPUTS=[userID,fullname,email,username,x_link,instagram_link,facebook_link,linkedin_link]'),
    path('login',views.user_login,name="[POST] ETKİ=[Giriş yapar] INPUTS=[email,password]"),
    path('register',views.user_register,name="[POST] ETKİ=[Kayıt İşlemi] INPUTS=[full_name,email,password]"),
    path('logout',views.user_logout,name="[POST] ETKİ=[çıkış] INPUTS=[]"),
    path('delete',views.delete_user,name="[POST] ETKİ=[Kullanıcı Silme] INPUTS=[userID]"),
    path('changepassword',views.change_password,name="[POST] ETKİ=[Kullanıcı Şifre Değiştirme] INPUTS=[userID,current_password,new_password]"),
]
