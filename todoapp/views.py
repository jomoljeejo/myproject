# todoapp/views.py
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from todoapp.model.model import Todo
from todoapp.serializer.request import (
    CreateTodoSerializer,
    UpdateTodoSerializer,
    PartialUpdateTodoSerializer,
)

def create_todo(request):
    serializer = CreateTodoSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    todo = Todo.objects.create(**serializer.validated_data)
    return Response({
        "id": todo.id,
        "title": todo.title,
        "description": todo.description,
        "is_done": todo.is_done,
    }, status=status.HTTP_201_CREATED)

def list_todos(request):
    todos = Todo.objects.all().order_by('id')
    return Response([
        {
            "id": t.id,
            "title": t.title,
            "description": t.description,
            "is_done": t.is_done,
        }
        for t in todos
    ], status=status.HTTP_200_OK)

def retrieve_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    return Response({
        "id": todo.id,
        "title": todo.title,
        "description": todo.description,
        "is_done": todo.is_done,
    }, status=status.HTTP_200_OK)

def update_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)

    if request.method == "PUT":
        serializer = UpdateTodoSerializer(data=request.data)
    else:
        serializer = PartialUpdateTodoSerializer(data=request.data, partial=True)

    serializer.is_valid(raise_exception=True)

    for field, value in serializer.validated_data.items():
        setattr(todo, field, value)
    todo.save()

    return Response({
        "id": todo.id,
        "title": todo.title,
        "description": todo.description,
        "is_done": todo.is_done,
    }, status=status.HTTP_200_OK)

def delete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
