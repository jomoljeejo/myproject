from rest_framework import serializers
from feature.artistapp.dataclass.request.update import UpdateArtistRequest

class UpdateArtistRequestSerializer(serializers.Serializer):
    artist_id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    country = serializers.CharField(
        required=False,
        allow_null=True,
        allow_blank=True
    )

    def create(self, validated_data):
        return UpdateArtistRequest(
            artist_id=validated_data["artist_id"],
            name=validated_data["name"],
            country=validated_data.get("country")
        )
