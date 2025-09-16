# Delete Book

```python
from bookshelf.models import Book

# Retrieve the book by title
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()
