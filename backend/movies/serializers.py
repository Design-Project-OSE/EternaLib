from rest_framework import serializers
from .models import Movies_Table,Movies_Comment,Movies_Category,Movies_Like

class Seri_movietable(serializers.ModelSerializer):
    class Meta:
        model=Movies_Table
        fields=('__all__')
        
class Seri_moviecategory(serializers.ModelSerializer):
    class Meta:
        model=Movies_Category
        fields=('__all__')
        
class Seri_moviecomment(serializers.ModelSerializer):
    class Meta:
        model=Movies_Comment
        fields=('__all__')
        
class Seri_movielike(serializers.ModelSerializer):
    class Meta:
        model=Movies_Comment
        fields=('__all__')