from rest_framework.decorators import api_view
from project.feature.todoapp import views


@api_view(['POST'])
def create_todo(request):
    return views.create_todo(request)


@api_view(['GET'])
def list_todos(request):
    return views.list_todos(request)


@api_view(['GET'])
def retrieve_todo(request):
    return views.retrieve_todo(request)


@api_view(['PUT', 'PATCH'])
def update_todo(request):
    return views.update_todo(request)


@api_view(['DELETE'])
def delete_todo(request):
    return views.delete_todo(request)


__all__ = [
    "create_todo",
    "list_todos",
    "retrieve_todo",
    "update_todo",
    "delete_todo",
]
