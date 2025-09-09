# relationship_app/urls.py
from django.urls import path
from . import views

app_name = "relationship_app"

urlpatterns = [
    # Function-based view
    path("books/", views.list_books, name="list_books"),

    # Class-based view using library primary key
    # Example: /libraries/1/ will show library with pk=1
    path("libraries/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),
]
