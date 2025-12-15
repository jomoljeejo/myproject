from rest_framework import serializers

class TodoListItemSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    is_done = serializers.BooleanField()
    created_at = serializers.DateTimeField()
