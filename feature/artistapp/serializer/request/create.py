
from rest_framework import serializers
from feature.artistapp.dataclass.request.create import CreateArtistRequest

class CreateArtistSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    country = serializers.CharField(
        required=False,
        allow_blank=True,
        allow_null=True
    )

    def create(self, validated_data):
        return CreateArtistRequest(
            tableName=validated_data["name"],
            country=validated_data.get("country")
        )
