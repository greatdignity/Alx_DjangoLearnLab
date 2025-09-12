
# Register your models here.
from django.contrib import admin
from .models import Book

# Basic registration
# admin.site.register(Book)

# Customized admin class
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')
    list_filter = ('published_date',)

