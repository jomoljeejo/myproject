from rest_framework import serializers
from feature.artistapp.dataclass.request.list import ListArtistRequest

class ListArtistRequestSerializer(serializers.Serializer):
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
        return ListArtistRequest(
            page_num=validated_data.get("page_num", 1),
            limit=validated_data.get("limit", 10)
        )
