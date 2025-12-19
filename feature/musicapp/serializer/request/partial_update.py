from rest_framework import serializers


class PartialUpdateMusicSerializer(serializers.Serializer):
    title = serializers.CharField(required=False)
    artist = serializers.CharField(required=False)
    album = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    genre = serializers.CharField(required=False, allow_null=True, allow_blank=True)
