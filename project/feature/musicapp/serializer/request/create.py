from rest_framework import serializers

class CreateMusicSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    artist = serializers.CharField(max_length=255)
    album = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    genre = serializers.CharField(required=False, allow_blank=True, allow_null=True)
