from django.contrib import admin
from .models import Movies_Table,Movies_Genres_Table

class MoviesAdmin(admin.ModelAdmin):
    list_display=('id','name','savedate','isPublished')
    list_display_links=('id','name')
    list_filter=['savedate']
    list_editable=('isPublished',)
    search_fields=('id','name','about','genres')
    list_per_page=10
    
class Movies_GenresAdmin(admin.ModelAdmin):
    list_display=('gen_id','savedate')
    list_display_links=('gen_id',)
    list_filter=['savedate']
    search_fields=('id','name')
    list_per_page=10
    
admin.site.register(Movies_Table,MoviesAdmin)
admin.site.register(Movies_Genres_Table,Movies_GenresAdmin)