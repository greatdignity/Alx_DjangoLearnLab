import os
import sys
import django

# Add project root (directory containing manage.py) to sys.path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# Set Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")

# Setup Django
django.setup()

# Now you can safely import models
from django.contrib.auth.models import Permission
from relationship_app.models import Book

# This will ensure permissions are created
from django.contrib.contenttypes.models import ContentType

book_content_type = ContentType.objects.get_for_model(Book)

# Just to check
for perm in Permission.objects.filter(content_type=book_content_type):
    print(perm.codename, "→", perm.name)
