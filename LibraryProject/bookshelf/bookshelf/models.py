from django.conf import settings
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    added_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # CustomUser again
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

    class Meta:  # 👈 This must be INSIDE the Book model
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_edit_book", "Can edit book"),
            ("can_delete_book", "Can delete book"),
        ]
