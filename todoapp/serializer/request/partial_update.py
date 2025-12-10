from rest_framework import serializers
from todoapp.dataclass.request.partial_update import TodoPartialUpdateDTO

class TodoPartialUpdateRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255, required=False)
    description = serializers.CharField(allow_blank=True, required=False)
    is_done = serializers.BooleanField(required=False)

def to_partial_update_dto(serializer: TodoPartialUpdateRequestSerializer) -> TodoPartialUpdateDTO:
    d = serializer.validated_data
    return TodoPartialUpdateDTO(
        id=d["id"],
        title=d.get("title"),
        description=d.get("description"),
        is_done=d.get("is_done"),
    )
