from rest_framework import serializers

class UpdateTodoSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255, required=False)
    description = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    is_done = serializers.BooleanField(required=False)

    def validate(self, attrs):
        # ensure at least one updatable field present
        if not attrs:
            raise serializers.ValidationError("At least one field must be provided for update.")
        return attrs
