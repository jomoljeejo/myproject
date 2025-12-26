from rest_framework.decorators import api_view
from rest_framework.request import Request

from feature.todoapp.views import TodoView
from feature.todoapp.serializer.request import (
    CreateTodoSerializer,
    UpdateTodoSerializer,
    PartialUpdateTodoSerializer,
    RetrieveTodoSerializer,
    TodoDeleteRequestSerializer,
    ListTodoRequestSerializer,
)
from feature.common.utilities import Utils


class TodoController:
    view = TodoView()


    @staticmethod
    @api_view(["POST"])
    def create(request: Request):
        serializer = CreateTodoSerializer(data=request.data)
        validation = Utils.validate(serializer)
        if validation is not True:
            return validation

        return TodoController.view.create(serializer.validated_data)


    @staticmethod
    @api_view(["GET"])
    def get_all(request: Request):
        serializer = ListTodoRequestSerializer(data=request.query_params)
        validation = Utils.validate(serializer)
        if validation is not True:
            return validation

        return TodoController.view.list_todo(serializer.validated_data)


    @staticmethod
    @api_view(["GET"])
    def get_one(request: Request):
        serializer = RetrieveTodoSerializer(data=request.query_params)
        validation = Utils.validate(serializer)
        if validation is not True:
            return validation

        return TodoController.view.retrieve(serializer.validated_data)

    @staticmethod
    @api_view(["PUT", "PATCH"])
    def update(request: Request):
        data = request.data.copy()

        todo_id = request.query_params.get("id")
        if not todo_id:
            return Utils.error_response("id is required")

        data["id"] = int(todo_id)

        serializer = (
            UpdateTodoSerializer(data=data)
            if request.method == "PUT"
            else PartialUpdateTodoSerializer(data=data, partial=True)
        )

        validation = Utils.validate(serializer)
        if validation is not True:
            return validation

        return TodoController.view.update(serializer.validated_data)


    @staticmethod
    @api_view(["DELETE"])
    def delete(request: Request):
        data = request.data.copy()

        todo_id = request.query_params.get("id")
        if not todo_id:
            return Utils.error_response("id is required")

        data["id"] = int(todo_id)

        serializer = TodoDeleteRequestSerializer(data=data)
        validation = Utils.validate(serializer)
        if validation is not True:
            return validation

        return TodoController.view.delete(serializer.validated_data)

