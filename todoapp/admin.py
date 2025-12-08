from django.contrib import admin
from todoapp.model.model import Todo

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_completed', 'created_at')
    list_filter = ('is_completed',)
    search_fields = ('title', 'description')

