from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from common.utilities import Utils
from todoapp.model.model import Todo
from todoapp.serializer.request import (
    CreateTodoSerializer,
    UpdateTodoSerializer,
    PartialUpdateTodoSerializer,
)
from todoapp.serializer.response.todo_detail import TodoDetailResponseSerializer


def create_todo(request):
    serializer = CreateTodoSerializer(data=request.data)

    validation = Utils.validate(serializer)
    if validation is not True:
        return validation

    todo = Todo.objects.create(**serializer.validated_data)

    data = TodoDetailResponseSerializer.serialize(todo)

    return Response(
        Utils.success_response(
            message="Todo created successfully",
            data=data
        ),
        status=status.HTTP_201_CREATED
    )


def list_todos(request):
    todos = Todo.objects.all().order_by("id")

    data = [
        TodoDetailResponseSerializer.serialize(todo)
        for todo in todos
    ]

    return Response(
        Utils.success_response(
            message="Todos fetched successfully",
            data=data
        ),
        status=status.HTTP_200_OK
    )


def retrieve_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)

    data = TodoDetailResponseSerializer.serialize(todo)

    return Response(
        Utils.success_response(
            message="Data fetched successfully",
            data=data
        ),
        status=status.HTTP_200_OK
    )


def update_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)

    if request.method == "PUT":
        serializer = UpdateTodoSerializer(data=request.data)
    else:
        serializer = PartialUpdateTodoSerializer(
            data=request.data,
            partial=True
        )

    validation = Utils.validate(serializer)
    if validation is not True:
        return validation

    for field, value in serializer.validated_data.items():
        setattr(todo, field, value)
    todo.save()

    data = TodoDetailResponseSerializer.serialize(todo)

    return Response(
        Utils.success_response(
            message="Todo updated successfully",
            data=data
        ),
        status=status.HTTP_200_OK
    )


def delete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()

    return Response(
        Utils.success_response(
            message="Todo deleted successfully"
        ),
        status=status.HTTP_200_OK
    )
