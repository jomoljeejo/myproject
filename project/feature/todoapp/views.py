from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from common.utilities import Utils
from project.feature.todoapp.model.model import Todo
from project.feature.todoapp.serializer.request import (
    CreateTodoSerializer,
    UpdateTodoSerializer,
    PartialUpdateTodoSerializer,
)
from project.feature.todoapp.serializer.response.todo_detail import TodoDetailResponseSerializer



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



def retrieve_todo(request):
    table_code = request.GET.get("tableCode")

    if not table_code:
        return Response(
            Utils.error_response(
                message="tableCode is required",
                error="Missing query parameter: tableCode"
            ),
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        todo_id = int(table_code.split("-")[-1])
    except (ValueError, AttributeError):
        return Response(
            Utils.error_response(
                message="Invalid tableCode format",
                error="Expected format: TODO-<id>"
            ),
            status=status.HTTP_400_BAD_REQUEST
        )

    todo = get_object_or_404(Todo, id=todo_id)

    data = TodoDetailResponseSerializer.serialize(todo)

    return Response(
        Utils.success_response(
            message="Data fetched successfully",
            data=data
        ),
        status=status.HTTP_200_OK
    )



def update_todo(request):
    table_code = request.GET.get("tableCode")

    if not table_code:
        return Response(
            Utils.error_response(
                message="tableCode is required",
                error="Missing query parameter: tableCode"
            ),
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        todo_id = int(table_code.split("-")[-1])
    except (ValueError, AttributeError):
        return Response(
            Utils.error_response(
                message="Invalid tableCode format",
                error="Expected format: TODO-<id>"
            ),
            status=status.HTTP_400_BAD_REQUEST
        )

    todo = get_object_or_404(Todo, id=todo_id)

    serializer = (
        UpdateTodoSerializer(data=request.data)
        if request.method == "PUT"
        else PartialUpdateTodoSerializer(data=request.data, partial=True)
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



def delete_todo(request):
    table_code = request.GET.get("tableCode")

    if not table_code:
        return Response(
            Utils.error_response(
                message="tableCode is required",
                error="Missing query parameter: tableCode"
            ),
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        todo_id = int(table_code.split("-")[-1])
    except (ValueError, AttributeError):
        return Response(
            Utils.error_response(
                message="Invalid tableCode format",
                error="Expected format: TODO-<id>"
            ),
            status=status.HTTP_400_BAD_REQUEST
        )

    todo = get_object_or_404(Todo, id=todo_id)
    todo.delete()

    return Response(
        Utils.success_response(
            message="Todo deleted successfully"
        ),
        status=status.HTTP_200_OK
    )
