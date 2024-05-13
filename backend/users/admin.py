from django.contrib import admin
from .models import Users_MovieComment,Users_BookComment,Users_GameComment

class MoviesAdmin(admin.ModelAdmin):
    list_display=('__all__')
    list_display_links=('userID','movieID','savedate')
    list_filter=['savedate']
    list_editable=('isPublished',)
    search_fields=('userID','movieID')
    list_per_page=10
    
class GamesAdmin(admin.ModelAdmin):
    list_display=('__all__')
    list_display_links=('userID','bookID','savedate')
    list_filter=['savedate']
    list_editable=('isPublished',)
    search_fields=('userID','movieID')
    list_per_page=10
    
class BookAdmin(admin.ModelAdmin):
    list_display=('__all__')
    list_display_links=('userID','gameID','savedate')
    list_filter=['savedate']
    list_editable=('isPublished',)
    search_fields=('userID','movieID')
    list_per_page=10
    
admin.site.register(Users_MovieComment,MoviesAdmin)
admin.site.register(Users_BookComment,GamesAdmin)
admin.site.register(Users_GameComment,GamesAdmin)