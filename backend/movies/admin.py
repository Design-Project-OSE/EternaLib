from django.contrib import admin
from .models import Movies_Table, Movies_Category, Movies_Comment, Movies_Like

class MoviesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'savedate', 'isPublished')
    list_display_links = ('id', 'name')
    list_filter = ['savedate']
    list_editable = ('isPublished',)
    search_fields = ['id', 'name', 'about']  # 'genres' alanını kaldırdım, bu alan modelde tanımlı değil
    list_per_page = 10

    class Meta:
        verbose_name = "Filmler"
        verbose_name_plural = "Filmler"

class Movies_Category_Admin(admin.ModelAdmin):
    list_display = ('id', 'catshort', 'name', 'savedate')
    list_display_links = ('id', 'name')
    list_filter = ['savedate']
    search_fields = ['id', 'name', 'catshort']
    list_per_page = 10

    class Meta:
        verbose_name = "Film Kategorileri"
        verbose_name_plural = "Film Kategorileri"

class Movies_Comment_Admin(admin.ModelAdmin):
    list_display = ('id', 'movieID', 'userID', 'comment', 'savedate')
    list_display_links = ('id', 'movieID')  # 'name' yerine 'movieID' kullandım
    list_filter = ['savedate']
    search_fields = ['id', 'movieID', 'userID', 'comment']
    list_per_page = 10

    class Meta:
        verbose_name = "Film Yorum"
        verbose_name_plural = "Film Yorumları"

class Movies_Like_Admin(admin.ModelAdmin):
    list_display = ('id', 'userID', 'movieID', 'savedate')
    list_display_links = ('id', 'userID', 'movieID')
    list_filter = ['savedate']
    search_fields = ['id', 'userID', 'movieID']
    list_per_page = 10

    class Meta:
        verbose_name = "Film Beğeni"
        verbose_name_plural = "Film Beğeniler"

admin.site.register(Movies_Table, MoviesAdmin)
admin.site.register(Movies_Category, Movies_Category_Admin)
admin.site.register(Movies_Comment, Movies_Comment_Admin)
admin.site.register(Movies_Like, Movies_Like_Admin)
