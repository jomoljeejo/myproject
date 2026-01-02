from rest_framework import serializers

class CreateArtistSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    country = serializers.CharField(
        required=False,
        allow_blank=True,
        allow_null=True
    )
