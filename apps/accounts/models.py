from django.contrib.auth.models import User
from django.db import models


class UserType(models.TextChoices):
    # ADMIN = "admin", "Admin"
    SPECIFIER = "specifier", "Specifier"
    REVIEWER = "reviewer", "Reviewer"


class UserPermissions(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(
        max_length=20, choices=UserType.choices, default=UserType.SPECIFIER
    )

    def __str__(self):
        return f"{self.user.username} - ({self.user_type})"
