from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Расширенная модель пользователя."""

    class Roles(models.TextChoices):
        DEVELOPER = "developer"
        MANAGER = "manager"
        ADMIN = "admin"

    role = models.CharField(
        max_length=255, default=Roles.DEVELOPER, choices=Roles.choices
    )
    date_of_birth = models.DateField(null=True, verbose_name="Date of birth")
    phone = models.CharField(max_length=20, null=True, verbose_name="Phone")

    def __str__(self):
        return self.username
