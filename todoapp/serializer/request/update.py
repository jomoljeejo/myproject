from rest_framework import serializers
from todoapp.dataclass.request.update import TodoUpdateDTO

class TodoUpdateRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255, required=False)
    description = serializers.CharField(allow_blank=True, required=False)
    is_done = serializers.BooleanField(required=False)

def to_update_dto(serializer: TodoUpdateRequestSerializer) -> TodoUpdateDTO:
    d = serializer.validated_data
    return TodoUpdateDTO(
        id=d["id"],
        title=d.get("title"),
        description=d.get("description"),
        is_done=d.get("is_done"),
    )
