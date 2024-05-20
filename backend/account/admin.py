from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.http import JsonResponse

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'full_name', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('full_name',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Links', {'fields': ('username', 'x_link', 'instagram_link', 'facebook_link', 'linkedin_link')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'full_name', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)

def update_user_info(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        if user_id:
            try:
                user = CustomUser.objects.get(id=user_id)
                # Yeni bilgileri al
                full_name = request.POST.get('full_name')
                email = request.POST.get('email')
                username = request.POST.get('username')
                x_link = request.POST.get('x_link')
                instagram_link = request.POST.get('instagram_link')
                facebook_link = request.POST.get('facebook_link')
                linkedin_link = request.POST.get('linkedin_link')

                # Yeni bilgileri güncelle
                user.full_name = full_name
                user.email = email
                user.username = username
                user.x_link = x_link
                user.instagram_link = instagram_link
                user.facebook_link = facebook_link
                user.linkedin_link = linkedin_link

                # Değişiklikleri kaydet
                user.save()

                return JsonResponse({'success': 'User information updated successfully'})
            except CustomUser.DoesNotExist:
                return JsonResponse({'error': 'User does not exist'}, status=404)
        else:
            return JsonResponse({'error': 'User ID is required'}, status=400)
    else:
        return JsonResponse({'error': 'POST method is required'}, status=405)