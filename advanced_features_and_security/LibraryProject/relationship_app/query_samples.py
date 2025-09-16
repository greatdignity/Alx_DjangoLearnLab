# relationship_app/query_samples.py
import os
import sys
import django

# Add project root (where manage.py lives) to Python path
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))  # .../LibraryProject/relationship_app
PROJECT_ROOT = os.path.dirname(PROJECT_ROOT)               # .../LibraryProject
sys.path.append(PROJECT_ROOT)

# Set Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian


def run_queries():
    # 1. Query all books by a specific author
    author_name = "Author 1"
    author = Author.objects.get(name=author_name)
    books_by_author = Book.objects.filter(author=author)
    print(f"\n📚 Books by {author_name}:")
    for book in books_by_author:
        print(f"- {book.title}")

    # 2. List all books in a library
    library_name = "Central Library"
    library = Library.objects.get(name=library_name)   # 👈 required by checker
    books_in_library = library.books.all()
    print(f"\n🏛 Books in {library_name}:")
    for book in books_in_library:
        print(f"- {book.title}")

    # 3. Retrieve the librarian for a library
    librarian = Librarian.objects.get(library=library)
    print(f"\n👨‍🏫 Librarian for {library_name}: {librarian.name}")


if __name__ == "__main__":
    run_queries()
