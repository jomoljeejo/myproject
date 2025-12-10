from rest_framework import serializers
from todoapp.dataclass.request.delete import TodoDeleteDTO

class TodoDeleteRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField()

def to_delete_dto(serializer: TodoDeleteRequestSerializer) -> TodoDeleteDTO:
    d = serializer.validated_data
    return TodoDeleteDTO(id=d["id"])
