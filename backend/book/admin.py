from django.contrib import admin
from .models import Book_Category, Book_Table, Book_Comment, Book_Like

class Book_Admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'savedate', 'isPublished')
    list_display_links = ('id', 'name', 'savedate')
    list_filter = ['savedate']
    list_editable = ('isPublished',)
    search_fields = ['bookID', 'name']
    list_per_page = 10

    class Meta:
        verbose_name = "Kitap"
        verbose_name_plural = "Kitaplar"
    
class Book_Category_Admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'catshort', 'savedate')
    list_display_links = ('id', 'name', 'catshort', 'savedate')
    list_filter = ['savedate']
    search_fields = ['bookID', 'name']
    list_per_page = 10

    class Meta:
        verbose_name = "Kitap Kategori"
        verbose_name_plural = "Kitap Kategorileri"

class Book_Comment_Admin(admin.ModelAdmin):
    list_display = ('id', 'userID', 'bookID', 'comment', 'savedate')
    list_display_links = ('id', 'userID', 'bookID', 'comment', 'savedate')
    list_filter = ['savedate']
    search_fields = ['bookID', 'id', 'userID', 'comment']
    list_per_page = 10

    class Meta:
        verbose_name = "Kitap Yorumu"
        verbose_name_plural = "Kitap Yorumları"
        
class Book_Like_Admin(admin.ModelAdmin):
    list_display = ('id', 'userID', 'bookID', 'savedate')
    list_display_links = ('id', 'userID', 'bookID', 'savedate')
    list_filter = ['savedate']
    search_fields = ['bookID', 'id', 'userID']
    list_per_page = 10

    class Meta:
        verbose_name = "Kitap Beğeni"
        verbose_name_plural = "Kitap Beğenileri"
    
admin.site.register(Book_Category, Book_Category_Admin)
admin.site.register(Book_Table, Book_Admin)
admin.site.register(Book_Comment, Book_Comment_Admin)
admin.site.register(Book_Like, Book_Like_Admin)
