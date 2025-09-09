# Create your views here.
# relationship_app/views.py
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import DetailView
from django.template import loader, TemplateDoesNotExist

from .models import Book, Library


def list_books(request):
    """
    Function-based view that lists all books (title + author).
    Renders a template if present; falls back to plain text.
    """
    books = Book.objects.select_related("author").all()

    # Try to render the template (recommended)
    try:
        template = loader.get_template("relationship_app/list_books.html")
        return HttpResponse(template.render({"books": books}, request))
    except TemplateDoesNotExist:
        # Fallback: plain text response (useful if you haven't added templates yet)
        lines = [f"{b.title} by {b.author.name}" for b in books]
        return HttpResponse("\n".join(lines), content_type="text/plain")


class LibraryDetailView(DetailView):
    """
    Class-based view (DetailView) that displays a Library and its books.
    URL will provide the library primary key (pk).
    """
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

    # (Optional) you can override get_context_data if you want extra context:
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        # Ensure books are prefetched for performance
        ctx["books"] = self.object.books.select_related("author").all()
        return ctx
