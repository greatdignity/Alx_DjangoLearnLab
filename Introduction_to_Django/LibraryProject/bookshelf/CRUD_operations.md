# Create Operation

# CRUD Operations with Django Models

This document demonstrates the Create, Retrieve, Update, and Delete operations on the `Book` model using Django’s ORM.

---

## Create Operation

```python
from bookshelf.models import Book

# Create a new Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
# Expected Output
<Book: 1984 by George Orwell (1949)>


# Retrieve Operation
from bookshelf.models import Book


# Retrieve all books
books = Book.objects.all()
for b in books:
    print(b.title, b.author, b.publication_year)

# Expected Output 
1984 George Orwell 1949

# Update Operation
from bookshelf.models import Book

# Retrieve the book and update the title
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book

#Expected Output
<Book: Nineteen Eighty-Four by George Orwell (1949)>


# Delete Operation
from bookshelf.models import Book

# Delete the book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion
Book.objects.all()

#Expected Output
<QuerySet []>
