from rest_framework import serializers
from feature.musicapp.dataclass.request.delete import DeleteMusicRequest

class DeleteMusicSerializer(serializers.Serializer):
    tableCode = serializers.CharField()

    def create(self, validated_data):
        return DeleteMusicRequest(
            tableCode=validated_data["tableCode"]
        )

