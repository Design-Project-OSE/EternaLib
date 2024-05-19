from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile,CustomUser


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['full_name', 'liked_movies', 'liked_games', 'liked_books', 'profile_picture', 'x_link','instagram_link', 'facebook_link', 'linkedin_link','about']

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('first_name', 'last_name', 'email')

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user