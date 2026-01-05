from rest_framework import serializers
from feature.musicapp.dataclass.request.list import ListMusicRequest

class ListMusicRequestSerializer(serializers.Serializer):
    page_num = serializers.IntegerField(
        min_value=1,
        required=False,
        default=1
    )
    limit = serializers.IntegerField(
        min_value=1,
        required=False,
        default=10
    )

    def create(self, validated_data):
        return ListMusicRequest(
            page_num=validated_data.get("page_num", 1),
            limit=validated_data.get("limit", 10)
        )
