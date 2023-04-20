from django.core.validators import MinLengthValidator
from django.db import models


class Tag(models.Model):
    """Модель Тегов"""

    name = models.CharField(
        max_length=20, verbose_name="Name", validators=[MinLengthValidator(1)]
    )

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.name
