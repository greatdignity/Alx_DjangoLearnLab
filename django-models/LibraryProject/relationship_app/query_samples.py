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

# Example queries
def run_queries():
    print("\n📚 All Books:")
    for book in Book.objects.all():
        print(f"- {book.title} by {book.author.name}")

    print("\n🏛 Libraries and their Books:")
    for library in Library.objects.all():
        print(f"{library.name}: {[book.title for book in library.books.all()]}")

    print("\n👨‍🏫 Librarians and their Libraries:")
    for librarian in Librarian.objects.all():
        print(f"{librarian.name} manages {librarian.library.name}")


if __name__ == "__main__":
    run_queries()
