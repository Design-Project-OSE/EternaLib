from rest_framework import serializers
from .models import CustomUser, UserProfile

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'is_staff', 'is_active']
        read_only_fields = ['id', 'is_staff', 'is_active']

class UserProfileSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = UserProfile
        fields = ['id', 'user']
        read_only_fields = ['id']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = CustomUser.objects.create(**user_data)
        user_profile = UserProfile.objects.create(user=user, **validated_data)
        return user_profile

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        user = instance.user

        instance.user.email = user_data.get('email', user.email)
        instance.user.is_active = user_data.get('is_active', user.is_active)
        instance.user.is_staff = user_data.get('is_staff', user.is_staff)
        instance.user.save()

        instance.save()
        return instance
