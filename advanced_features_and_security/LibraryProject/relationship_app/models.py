from django.db import models
from django.conf import settings

# relationship_app/models.py
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    published_date = models.DateField()

    class Meta:
        permissions = [
            ("can_view", "Can view book"),
            ("can_create", "Can create book"),
            ("can_edit", "Can edit book"),
            ("can_delete", "Can delete book"),
        ]

        
    def __str__(self):
        return self.title


class Relationship(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    friend = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='friends',
        on_delete=models.CASCADE
    )
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.user} - {self.friend} ({self.status})"

# Custom permissions defined for Book model to manage access control.