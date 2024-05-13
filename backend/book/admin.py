from django.contrib import admin
from .models import category_book,Book_Table


    
class Book_Admin(admin.ModelAdmin):
    list_display=('__all__')
    list_display_links=('bookID','name','savedate','isPublished')
    list_filter=['savedate']
    list_editable=('isPublished',)
    search_fields=('bookID','name')
    list_per_page=10
    
class Book_Category_Admin(admin.ModelAdmin):
    list_display=('__all__')
    list_display_links=('bookID','name','savedate')
    list_filter=['savedate']
    search_fields=('bookID','name')
    list_per_page=10
    
admin.site.register(category_book,Book_Category_Admin)
admin.site.register(Book_Table,Book_Admin)
