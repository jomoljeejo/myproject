from rest_framework import serializers


class RetrieveMusicSerializer(serializers.Serializer):
    tableCode = serializers.CharField()
