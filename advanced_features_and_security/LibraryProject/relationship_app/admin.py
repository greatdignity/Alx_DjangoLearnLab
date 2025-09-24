# Register your models here.
from django.contrib import admin
from .models import Relationship

admin.site.register(Relationship)

from .models import Book

admin.site.register(Book)

