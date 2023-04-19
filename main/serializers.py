from rest_framework import serializers
from .models import Tag, Task, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "role",
            "first_name",
            "last_name",
            "email",
            "date_of_birth",
            "phone",
        )
        read_only_fields = ("id",)


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            "id",
            "name",
        )
        read_only_fields = ("id",)


class TaskSerializer(serializers.ModelSerializer):
    assigned_to = UserSerializer()
    creator = UserSerializer()
    tags = TagSerializer(many=True)

    class Meta:
        model = Task
        fields = (
            "id",
            "tags",
            "status",
            "pub_date",
            "creator",
            "assigned_to",
            "name",
            "description",
        )
        read_only_fields = (
            "id",
            "assigned_to",
            "creator",
            "tags",
        )
