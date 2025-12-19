from rest_framework.decorators import api_view
from rest_framework.request import Request

from feature.todoapp.views import TodoView
from feature.todoapp.serializer.request import (
    CreateTodoSerializer,
    UpdateTodoSerializer,
    PartialUpdateTodoSerializer,
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


        return TodoController.view.create(request)


    @staticmethod
    @api_view(["GET"])
    def get_all(request: Request):
        return TodoController.view.list_todo(request)


    @staticmethod
    @api_view(["GET"])
    def get_one(request: Request):
        return TodoController.view.retrieve(request)


    @staticmethod
    @api_view(["PUT", "PATCH"])
    def update(request: Request):
        serializer = (
            UpdateTodoSerializer(data=request.data)
            if request.method == "PUT"
            else PartialUpdateTodoSerializer(data=request.data, partial=True)
        )

        validation = Utils.validate(serializer)
        if validation is not True:
            return validation

        return TodoController.view.update(request)


    @staticmethod
    @api_view(["DELETE"])
    def delete(request: Request):
        return TodoController.view.delete(request)
