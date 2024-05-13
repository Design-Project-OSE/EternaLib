from django.contrib import admin
from .models import category_game,Games_Table


    
class Games_Admin(admin.ModelAdmin):
    list_display=('__all__')
    list_display_links=('gameID','name','savedate','isPublished')
    list_filter=['savedate']
    list_editable=('isPublished',)
    search_fields=('gameID','name')
    list_per_page=10
    
class Game_Category_Admin(admin.ModelAdmin):
    list_display=('__all__')
    list_display_links=('gameID','name','savedate')
    list_filter=['savedate']
    search_fields=('gameID','name')
    list_per_page=10
    
admin.site.register(category_game,Game_Category_Admin)
admin.site.register(Games_Table,Games_Admin)
