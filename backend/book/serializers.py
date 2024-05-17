from rest_framework import serializers
from .models import category_book, Book_Table

class Seri_categorybook(serializers.ModelSerializer):
    class Meta:
        model = category_book
        fields = '__all__'
        
class Seri_booktable(serializers.ModelSerializer):
    class Meta:
        model = Book_Table
        fields = '__all__'
