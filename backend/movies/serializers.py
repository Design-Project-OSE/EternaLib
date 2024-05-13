from rest_framework import serializers
from .models import category_movie,Movies_Table

class Seri_movietable():
    class meta:
        model=Movies_Table
        fields=('name','url_name','production','about','category_id','release','isPublished',
                'imdb','metacritic','background','poster','trailer','savedate')
        
class Seri_categorymovie():
    class meta:
        model=category_movie
        fields=('category_id','name','savedate')
        
