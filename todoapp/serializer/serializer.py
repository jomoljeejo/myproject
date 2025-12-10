from rest_framework import serializers
from todoapp.model.model import Todo

class TodoSerializer(serializers.Serializer):
    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'is_completed', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
