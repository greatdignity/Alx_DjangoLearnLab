# relationship_app/seed_data.py
import os
import sys
import django

# Get the project root (the folder that contains manage.py)
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))  # .../LibraryProject/relationship_app
PROJECT_ROOT = os.path.dirname(PROJECT_ROOT)               # .../LibraryProject
sys.path.append(PROJECT_ROOT)

# Tell Django which settings to use
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian


def run():
    # Clear old demo data
    Author.objects.all().delete()
    Book.objects.all().delete()
    Library.objects.all().delete()
    Librarian.objects.all().delete()

    # Create authors
    achebe = Author.objects.create(name="Chinua Achebe")
    adichie = Author.objects.create(name="Chimamanda Ngozi Adichie")

    # Create books
    tfa = Book.objects.create(title="Things Fall Apart", author=achebe)
    noa = Book.objects.create(title="No Longer at Ease", author=achebe)
    hoa = Book.objects.create(title="Half of a Yellow Sun", author=adichie)

    # Create libraries
    central = Library.objects.create(name="Central Library")
    community = Library.objects.create(name="Community Library")

    # Many-to-many
    central.books.add(tfa, noa, hoa)
    community.books.add(noa)

    # One-to-one
    Librarian.objects.create(name="Mr. Adebayo", library=central)
    Librarian.objects.create(name="Ms. Kemi", library=community)

    print("✅ Seeded demo data.")


if __name__ == "__main__":
    run()
