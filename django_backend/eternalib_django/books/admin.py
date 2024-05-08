from django.contrib import admin
from .models import Books_Table,Books_Genres_Table

class BooksAdmin(admin.ModelAdmin):
    list_display=('id','name','savedate','isPublished')
    list_display_links=('id','name')
    list_filter=['savedate']
    list_editable=('isPublished',)
    search_fields=('id','name','about','genres')
    list_per_page=10
    
class Books_GenresAdmin(admin.ModelAdmin):
    list_display=('gen_id','savedate')
    list_display_links=('gen_id',)
    list_filter=['savedate']
    search_fields=('id','name')
    list_per_page=10
    
admin.site.register(Books_Table,BooksAdmin)

admin.site.register(Books_Genres_Table,Books_GenresAdmin)
