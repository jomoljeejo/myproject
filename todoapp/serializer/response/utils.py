from rest_framework import serializers

class PaginationSerializer(serializers.Serializer):
    page_num = serializers.IntegerField()
    limit = serializers.IntegerField()
    total_page = serializers.IntegerField()
    total_count = serializers.IntegerField()
    next_page_required = serializers.BooleanField()
    present_url = serializers.CharField()
