# todoapp/serializer/response/todo_detail.py
from rest_framework import serializers

class TodoResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    description = serializers.CharField(allow_blank=True, allow_null=True)
    is_done = serializers.BooleanField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

