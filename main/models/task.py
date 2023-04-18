from django.db import models
from .tag import Tag
from .user import User


class Task(models.Model):
    class Status(models.TextChoices):
        PLANNED = "planned"
        IN_PROGRESS = "in_progress"
        FINISHED = "finished"

    status = models.CharField(
        max_length=255, default=Status.PLANNED, choices=Status.choices
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")
    name = models.CharField(max_length=50, verbose_name="task")
    tag = models.ManyToManyField(Tag, verbose_name="tag")
    pub_date = models.DateTimeField(
        verbose_name="date",
        auto_now_add=True,
        db_index=True,
    )

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
        ordering = ("-pub_date",)
