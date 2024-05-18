from django.contrib import admin
from .models import Games_Table,Game_Category,Game_Comment,Game_Like


    
class Games_Admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'savedate', 'isPublished')  
    list_display_links = ('id', 'name', 'savedate')
    list_filter = ['savedate']
    list_editable = ('isPublished',)
    search_fields = ['gameID', 'name']
    list_per_page = 10
    class Meta:
        verbose_name = "Oyun"
        verbose_name_plural = "Oyunlar"
    
class Game_Category_Admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'savedate')  
    list_display_links = ('id', 'name', 'savedate')
    list_filter=['savedate']
    search_fields=('id','name')
    list_per_page=10
    class Meta:
        verbose_name = "Oyun Kategorisi"
        verbose_name_plural = "Oyun Kategorileri"
        
class Game_Comment_Admin(admin.ModelAdmin):
    list_display = ('id', 'userID', 'gameID', 'comment', 'savedate') 
    list_display_links = ('id', 'userID', 'gameID', 'savedate') 
    list_filter = ['savedate']
    search_fields = ['id', 'userID', 'gameID', 'comment']
    list_per_page = 10
    class Meta:
        verbose_name = "Oyun Yorumu"
        verbose_name_plural = "Oyun Yorumları"
        
class Game_Like_Admin(admin.ModelAdmin):
    list_display = ('id', 'userID', 'gameID', 'savedate')  
    list_display_links = ('id', 'userID', 'gameID', 'savedate')  
    list_filter = ['savedate']
    search_fields = ['id', 'userID', 'gameID']
    list_per_page = 10
    class Meta:
        verbose_name = "Oyun Beğeni"
        verbose_name_plural = "Oyun Beğenileri"
    
admin.site.register(Game_Category,Game_Category_Admin)
admin.site.register(Games_Table,Games_Admin)
admin.site.register(Game_Comment,Game_Comment_Admin)
admin.site.register(Game_Like,Game_Like_Admin)
