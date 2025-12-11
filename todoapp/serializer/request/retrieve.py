from rest_framework import serializers

class RetrieveTodoSerializer(serializers.Serializer):
    id = serializers.IntegerField(min_value=1)
