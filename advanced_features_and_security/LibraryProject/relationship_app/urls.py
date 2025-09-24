# relationship_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list, name='book_list'),            # view books
    path('books/add/', views.book_create, name='book_create'),    # add a book
    path('books/<int:pk>/edit/', views.book_edit, name='book_edit'),   # edit a book
    path('books/<int:pk>/delete/', views.book_delete, name='book_delete'),  # delete a book
]


