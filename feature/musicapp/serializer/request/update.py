from rest_framework import serializers


class UpdateMusicSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    artist = serializers.CharField(max_length=255)
    album = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    genre = serializers.CharField(required=False, allow_null=True, allow_blank=True)
