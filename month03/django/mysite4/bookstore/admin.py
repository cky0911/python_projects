from django.contrib import admin
from . import models


# Register your models here.
class BookManager(admin.ModelAdmin):
    list_display = ['id', 'title', 'pub', 'price', 'market_price']
    list_display_links = ['id', 'title']
    list_filter = ['pub']
    search_fields = ['title', 'pub']
    list_editable = ['market_price']


admin.site.register(models.Book, BookManager)


class AuthorManager(admin.ModelAdmin):
    list_display = ['id', 'name', 'age']


admin.site.register(models.Author, AuthorManager)
