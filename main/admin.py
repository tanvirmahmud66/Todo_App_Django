from django.contrib import admin
from .models import TodoModel
# Register your models here.


class TodoViews(admin.ModelAdmin):
    list_display = ("id", "todo", 'created', 'updated')


admin.site.register(TodoModel, TodoViews)
