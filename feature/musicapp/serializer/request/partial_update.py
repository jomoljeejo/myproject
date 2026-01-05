from rest_framework import serializers
from feature.musicapp.dataclass.request.partial_update import PartialUpdateMusicRequest

class PartialUpdateMusicSerializer(serializers.Serializer):
    title = serializers.CharField(required=False)
    artist = serializers.CharField(required=False)
    album = serializers.CharField(
        required=False,
        allow_blank=True,
        allow_null=True
    )
    genre = serializers.CharField(required=False)

    def validate(self, attrs):
        if not attrs:
            raise serializers.ValidationError(
                "At least one field must be provided for partial update."
            )
        return attrs

    def create(self, validated_data):
        return PartialUpdateMusicRequest(
            title=validated_data.get("title"),
            artist=validated_data.get("artist"),
            album=validated_data.get("album"),
            genre=validated_data.get("genre")
        )
