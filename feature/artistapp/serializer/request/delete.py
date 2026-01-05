from rest_framework import serializers
from feature.artistapp.dataclass.request.delete import DeleteArtistRequest

class DeleteArtistRequestSerializer(serializers.Serializer):
    artist_id = serializers.IntegerField()

    def create(self, validated_data):
        return DeleteArtistRequest(
            artist_id=validated_data["artist_id"]
        )
