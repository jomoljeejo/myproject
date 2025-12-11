# todoapp/serializer/request/create.py
from rest_framework import serializers

class CreateTodoSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    is_done = serializers.BooleanField(required=False, default=False)

    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("title cannot be blank")
        return value

    def create(self, validated_data):
        # optional convenience: return validated_data or create model instance
        return validated_data
