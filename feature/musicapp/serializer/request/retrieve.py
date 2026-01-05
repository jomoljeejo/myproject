from rest_framework import serializers
from feature.musicapp.dataclass.request.retrieve import RetrieveMusicRequest

class RetrieveMusicSerializer(serializers.Serializer):
    tableCode = serializers.CharField()

    def create(self, validated_data):
        return RetrieveMusicRequest(
            tableCode=validated_data["tableCode"]
        )
