from rest_framework.serializers import Serializer, ModelSerializer
from .models import Movies_Genres_Table, Movies_Table

class Seri_Genres(ModelSerializer):
    class Meta:
        model = Movies_Genres_Table
        fields = '__all__'

class Seri_Movie(ModelSerializer):
    class Meta:
        model = Movies_Table
        fields = '__all__'
