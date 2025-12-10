from rest_framework import serializers
from todoapp.dataclass.request.retrieve import TodoRetrieveDTO

class TodoRetrieveRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField()

def to_retrieve_dto(serializer: TodoRetrieveRequestSerializer) -> TodoRetrieveDTO:
    d = serializer.validated_data
    return TodoRetrieveDTO(id=d["id"])
