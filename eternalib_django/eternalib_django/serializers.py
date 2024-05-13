from rest_framework import serializers
from movies.models import Movies_Table,Movies_Genres_Table
from games.models import Games_Table,Games_Genres_Table
from books.models import Books_Table,Books_Genres_Table

class Movies_TableSerializers(serializers.ModelSerializer):
    class Meta:
        model=Movies_Table
        fields=('name','production','about','genres','release','imdb','metacritic',
                'background','poster','trailer','savedata','isPublished')
        
class Movies_Genres_TableSerializers(serializers.ModelSerializer):
    class Meta:
        model=Movies_Genres_Table
        fields=('name','gen_id','savedate')
        

class Games_TableSerializers(serializers.ModelSerializer):
    class Meta:
        model=Games_Table
        fields=('name','production','about','genres','release','imdb','metacritic',
                'background','poster','trailer','savedata','isPublished')
        
class Games_Genres_TableSerializers(serializers.ModelSerializer):
    class Meta:
        model=Games_Genres_Table
        fields=('name','gen_id','savedate')        
        

class Books_TableSerializers(serializers.ModelSerializer):
    class Meta:
        model=Books_Table
        fields=('name','production','about','genres','release',
                'background','poster','savedata','isPublished')
        
class Books_Genres_TableSerializers(serializers.ModelSerializer):
    class Meta:
        model=Books_Genres_Table
        fields=('name','gen_id','savedate')
        
from django.contrib.auth.models import Group, User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']