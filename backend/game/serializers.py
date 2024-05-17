from rest_framework import serializers
from .models import category_game,Games_Table

class Seri_gamestable(serializers.ModelSerializer):
    class meta:
        model=Games_Table
        fields=('name','url_name','production','about','category_id','release','isPublished',
                'imdb','metacritic','background','poster','trailer','savedate')
        
class Seri_category_games(serializers.ModelSerializer):
    class meta:
        model=category_game
        fields=('category_id','name','savedate')