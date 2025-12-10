

from django.contrib import admin
from .model.model import Todo  # adjust path if your model is elsewhere

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "is_done", "created_at")  # use is_done not is_completed
    list_filter = ("is_done", "created_at")
    search_fields = ("title", "description")
