from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .models import Tag
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'status',
        'author',
        'pub_date',
    )
    search_fields = (
        'name',
        'tag',
        'pub_date',
    )
    list_filter = (
        'name',
        'tag',
        'pub_date',
    )


class TagAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
    )
    search_fields = (
        'name',
    )
    list_filter = (
        'name',
    )
    empty_value_display = '-пусто-'


admin.site.register(User, UserAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Task, TaskAdmin)
