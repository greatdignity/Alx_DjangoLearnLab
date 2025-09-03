
# Register your models here.
from django.contrib import admin
from .models import Book

# Basic registration
# admin.site.register(Book)

# Customized admin class
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")  # show these in list view
    search_fields = ("title", "author")                     # add search bar
    list_filter = ("publication_year", "author")            # add filters
