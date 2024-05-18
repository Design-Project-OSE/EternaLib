from rest_framework import serializers
from .models import Games_Table,Game_Like,Game_Category,Game_Comment

class Seri_gamestable(serializers.ModelSerializer):
    class Meta:
        model=Games_Table
        fields=('__all__')
        
class Seri_gamescategory(serializers.ModelSerializer):
    class Meta:
        model=Game_Category
        fields=('__all__')
        
class Seri_gamescomment(serializers.ModelSerializer):
    class Meta:
        model=Game_Comment
        fields=('__all__')
        
class Seri_gameslike(serializers.ModelSerializer):
    class Meta:
        model=Game_Like
        fields=('__all__')