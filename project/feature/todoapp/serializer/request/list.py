from rest_framework import serializers

class ListTodoRequestSerializer(serializers.Serializer):
    page_num = serializers.IntegerField(min_value=1, default=1)
    limit = serializers.IntegerField(min_value=1, default=10)
    search = serializers.CharField(required=False, allow_blank=True, allow_null=True)
