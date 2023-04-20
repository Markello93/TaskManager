from django.core.validators import MinLengthValidator
from django.db import models
from .tag import Tag
from .user import User


class Task(models.Model):
    """Модель задач"""

    class Status(models.TextChoices):
        PLANNED = "planned"
        IN_PROGRESS = "in_progress"
        FINISHED = "finished"

    status = models.CharField(
        max_length=100, default=Status.PLANNED, choices=Status.choices, null=True
    )
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, related_name="creator"
    )
    assigned_to = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, related_name="assigned_to"
    )
    name = models.CharField(
        max_length=255, verbose_name="Name", validators=[MinLengthValidator(1)]
    )
    tags = models.ManyToManyField(Tag, verbose_name="Tags")
    description = models.CharField(null=True, verbose_name="Description")
    pub_date = models.DateTimeField(
        verbose_name="date",
        auto_now_add=True,
        db_index=True,
    )

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
        ordering = ("-pub_date",)

    def __str__(self):
        return self.name
