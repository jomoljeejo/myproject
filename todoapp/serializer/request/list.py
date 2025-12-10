from rest_framework import serializers
from todoapp.dataclass.request.list import TodoListQueryDTO

class TodoListRequestSerializer(serializers.Serializer):
    search = serializers.CharField(required=False, allow_blank=True)
    is_done = serializers.BooleanField(required=False)
    limit = serializers.IntegerField(required=False)
    offset = serializers.IntegerField(required=False)

def to_list_dto(serializer: TodoListRequestSerializer) -> TodoListQueryDTO:
    d = serializer.validated_data
    return TodoListQueryDTO(
        search=d.get("search"),
        is_done=d.get("is_done"),
        limit=d.get("limit", 100),
        offset=d.get("offset", 0),
    )
