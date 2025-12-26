from rest_framework import serializers


class UpdateMusicSerializer(serializers.Serializer):
    title = serializers.CharField(required=False)
    artist = serializers.CharField(required=False)
    album = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    duration = serializers.IntegerField(required=False)

    def validate(self, attrs):
        if not attrs:
            raise serializers.ValidationError(
                "At least one field must be provided for update."
            )
        return attrs
