from rest_framework import serializers


class TodoDeleteRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField()
