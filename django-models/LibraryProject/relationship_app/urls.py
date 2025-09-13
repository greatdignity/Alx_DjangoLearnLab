# relationship_app/urls.py
from django.urls import path
from .views import list_books, LibraryDetailView   # ✅ import both FBV and CBV
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path("books/", list_books, name="list_books"),  # function-based view
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),  # class-based view
]

from .views import list_books, LibraryDetailView, register_view, login_view, logout_view

urlpatterns = [
    path("books/", list_books, name="list_books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),
     # Registration (function-based view)
    path("register/", views.register, name="register"),

    # Login (class-based built-in view with template)
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),

    # Logout (class-based built-in view with template)
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
]


from . import views

urlpatterns = [
    path("admin-view/", views.admin_view, name="admin_view"),
    path("librarian-view/", views.librarian_view, name="librarian_view"),
    path("member-view/", views.member_view, name="member_view"),
]


urlpatterns = [
    # existing patterns...
    path("books/add/", views.add_book, name="add_book"),
    path("books/<int:pk>/edit/", views.edit_book, name="edit_book"),
    path("books/<int:pk>/delete/", views.delete_book, name="delete_book"),
]
