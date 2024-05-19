from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['full_name', 'favorite_movie', 'favorite_game', 'favorite_book', 'profile_picture', 'instagram_link', 'facebook_link', 'linkedin_link']
