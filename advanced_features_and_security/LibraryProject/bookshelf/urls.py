# LibraryProject/bookshelf/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='bookshelf_index'),
]
