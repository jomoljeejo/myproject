from rest_framework import serializers
from .todo_detail import TodoResponseSerializer

class TodoListResponseSerializer(serializers.Serializer):
    items = TodoResponseSerializer(many=True)
    total = serializers.IntegerField(required=False)
