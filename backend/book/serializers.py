from rest_framework import serializers
from .models import Book_Category, Book_Table,Book_Comment,Book_Like

class Seri_bookcategory(serializers.ModelSerializer):
    class Meta:
        model = Book_Category
        fields = '__all__'
        
class Seri_booktable(serializers.ModelSerializer):
    class Meta:
        model = Book_Table
        fields = '__all__'

class Seri_bookcomment(serializers.ModelSerializer):
    class Meta:
        model = Book_Comment
        fields = '__all__'
        
class Seri_booklike(serializers.ModelSerializer):
    class Meta:
        model = Book_Like
        fields = '__all__'