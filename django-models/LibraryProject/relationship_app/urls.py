# relationship_app/urls.py
from django.urls import path
from .views import list_books, LibraryDetailView   # ✅ import both FBV and CBV

urlpatterns = [
    path("books/", list_books, name="list_books"),  # function-based view
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),  # class-based view
]


from django.urls import path
from .views import list_books, LibraryDetailView, register_view, login_view, logout_view

urlpatterns = [
    path("books/", list_books, name="list_books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
]
