from rest_framework import serializers
from feature.musicapp.dataclass.request.create import CreateMusicRequest

class CreateMusicSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    artist = serializers.CharField(max_length=255)
    album = serializers.CharField(
        required=False,
        allow_blank=True,
        allow_null=True
    )
    duration = serializers.IntegerField(required=False)

    def create(self, validated_data):
        return CreateMusicRequest(
            title=validated_data["title"],
            artist=validated_data["artist"],
            album=validated_data.get("album"),
            duration=validated_data.get("duration")
        )
