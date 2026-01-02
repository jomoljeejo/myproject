

from rest_framework import serializers

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

