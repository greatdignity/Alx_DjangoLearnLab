# relationship_app/urls.py
from django.urls import path
from .views import list_books, LibraryDetailView   # ✅ import both FBV and CBV

urlpatterns = [
    path("books/", list_books, name="list_books"),  # function-based view
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),  # class-based view
]
