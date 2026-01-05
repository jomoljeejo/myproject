from rest_framework import serializers
from feature.artistapp.dataclass.request.retrive import RetrieveArtistRequest

class RetrieveArtistRequestSerializer(serializers.Serializer):
    artist_id = serializers.IntegerField()

    def create(self, validated_data):
        return RetrieveArtistRequest(
            artist_id=validated_data["artist_id"]
        )
