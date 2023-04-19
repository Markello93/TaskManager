from rest_framework import viewsets

from main.models import User, Tag, Task
from main.serializers import TagSerializer, TaskSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.order_by("id")
    serializer_class = UserSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.prefetch_related("tags")
    serializer_class = TagSerializer


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.select_related("creator", "assigned_to").prefetch_related(
            "tags"
        )
