from django.db import models


class Tag(models.Model):
    """Модель Тегов"""
    name = models.CharField(max_length=50, verbose_name="tag")

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.name
