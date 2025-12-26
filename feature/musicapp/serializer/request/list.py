from rest_framework import serializers


class ListMusicRequestSerializer(serializers.Serializer):
    page_num = serializers.IntegerField(min_value=1, default=1)
    limit = serializers.IntegerField(min_value=1, default=10)
