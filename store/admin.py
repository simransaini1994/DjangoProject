from django.contrib import admin

# Register your models here.
from store.models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'stock')


admin.site.register(Book, BookAdmin)
