from django.contrib.auth.decorators import permission_required
from django.shortcuts import render

@permission_required('bookshelf.can_add_book', raise_exception=True)
def add_book(request):
    # your code to handle adding a book
    return render(request, 'bookshelf/add_book.html')
