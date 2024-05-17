from rest_framework.serializers import Serializer
from .models import Movies_Genres_Table,Movies_Table

class Seri_Genres:
    class meta:
        model=Movies_Genres_Table
        fields=('__all__')
        
class Seri_Movie:
    class meta:
        model=Movies_Table
        fields=('__all__')