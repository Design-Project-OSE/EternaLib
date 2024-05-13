from rest_framework import serializers
from .models import category_book,Book_Table

class Seri_categorybook():
    class meta:
        model=category_book
        fields=('__all__',)
        
class Seri_booktable():
    class meta:
        model=Book_Table
        fields=('__all__',)