from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm, UserProfileForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            login(request, user)
            return redirect('profile')
    else:
        user_form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'user_form': user_form})

@login_required
def profile(request):
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, instance=request.user.userprofile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('profile')
    else:
        profile_form = UserProfileForm(instance=request.user.userprofile)
    return render(request, 'profile.html', {'profile_form': profile_form})
