from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class control_user:

    def cont_post(self,request) -> bool:
        return request.method == 'POST'

    def cont_username(self,request) -> bool:
        username = request.POST['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError('Username already exists')
        return True

    def cont_pass(self,request) -> bool:
        password = request.POST['password']
        repassword = request.POST['repassword']
        if password!= repassword:
            raise ValidationError('Passwords do not match')
        return True

    def cont_mail(self,request) -> bool:
        email = request.POST['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError('Email already exists')
        return True

    def start_cont(self,request):
        if not self.cont_post(request):
            raise ValidationError('Invalid request method')
        if not self.cont_pass(request):
            raise ValidationError('Passwords do not match')
        if not self.cont_username(request):
            raise ValidationError('Username already exists')
        if not self.cont_mail(request):
            raise ValidationError('Email already exists')
        user = User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password'],
            email=request.POST['email']
        )
        user.save()
        return 'User saved successfully'
    
import re

class control_password:
    def cont_len(self,paw: str) -> bool:
        return bool(len(paw) > 10)

    def cont_big(self,paw: str) -> bool:
        return any(char.isupper() for char in paw)

    def cont_spec(self,paw: str) -> bool:
        pattern = r'[^a-zA-Z0-9\s]'  
        return bool(re.search(pattern, paw))
    
    def start_cont(self,paw)->str:
        if not self.cont_big(paw):
            raise ValidationError('Please enter a capital letter!')
        if not self.cont_len(paw):
            raise ValidationError('Please enter a password of at least 10 characters!')
        if not self.cont_spec(paw):
            raise ValidationError('Please use special characters in your password!')
        return "successful"