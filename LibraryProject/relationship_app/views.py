from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect
from .models import Book

@permission_required('relationship_app.can_add_book')
def add_book(request):
    # logic to add a book
    return render(request, 'add_book.html')

@permission_required('relationship_app.can_edit_book')
def edit_book(request, pk):
    # logic to edit a book
    return render(request, 'edit_book.html')

@permission_required('relationship_app.can_delete_book')
def delete_book(request, pk):
    # logic to delete a book
    return redirect('book_list')
