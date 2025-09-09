# relationship_app/urls.py
from django.urls import path
from .views import list_books, LibraryDetailView   # ✅ import both FBV and CBV
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path("books/", list_books, name="list_books"),  # function-based view
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),  # class-based view
]


from django.urls import path
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


