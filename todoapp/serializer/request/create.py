from rest_framework import serializers
from todoapp.dataclass.request.create import TodoCreateDTO

class TodoCreateRequestSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(allow_blank=True, required=False)
    is_done = serializers.BooleanField(required=False, default=False)

def to_create_dto(serializer: TodoCreateRequestSerializer) -> TodoCreateDTO:
    d = serializer.validated_data
    return TodoCreateDTO(
        title=d["title"],
        description=d.get("description", "") or "",
        is_done=d.get("is_done", False),
    )
