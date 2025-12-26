from rest_framework import serializers


class DeleteMusicSerializer(serializers.Serializer):
    tableCode = serializers.CharField()
