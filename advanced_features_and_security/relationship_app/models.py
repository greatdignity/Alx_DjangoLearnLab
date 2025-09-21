from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()

    class Meta:
        permissions = [
            ("can_add_book", "Can add a new book"),
            ("can_edit_book", "Can edit a book"),
            ("can_delete_book", "Can delete a book"),
        ]

    def __str__(self):
        return self.title


from django.conf import settings  # best practice

class Relationship(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # points to CustomUser
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
