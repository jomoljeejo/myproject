from rest_framework.response import Response
from rest_framework import status
from django.core.paginator import Paginator

from feature.common.utilities import Utils
from feature.todoapp.model.model import Todo
from feature.todoapp.serializer.request import (
    CreateTodoSerializer,
    UpdateTodoSerializer,
    PartialUpdateTodoSerializer,
)
from feature.todoapp.serializer.response.todo_detail import (
    TodoDetailResponseSerializer
)


class TodoView:

    # ========================= CREATE =========================
    def create(self, request):
        serializer = CreateTodoSerializer(data=request.data)
        validation = Utils.validate(serializer)
        if validation is not True:
            return validation

        todo = Todo.create(**serializer.validated_data)

        data = TodoDetailResponseSerializer.serialize(todo)

        return Response(
            Utils.success_response(
                message="Todo created successfully",
                data=data
            ),
            status=status.HTTP_201_CREATED
        )

    # ========================= LIST =========================
    def list_todo(self, request):
        query_params = Utils.get_query_params(request)
        page_num = int(query_params.get("page_num", 1))
        limit = int(query_params.get("limit", 10))

        qs = Todo.get_all()

        paginator = Paginator(qs, limit)
        page = paginator.get_page(page_num)

        data = [
            TodoDetailResponseSerializer.serialize(todo)
            for todo in page.object_list
        ]

        paginated_data = Utils.add_page_parameter(
            final_data=data,
            page_num=page.number,
            total_page=paginator.num_pages,
            total_count=paginator.count,
            present_url=request.get_full_path(),
            next_page_required=True
        )

        return Response(
            Utils.success_response(
                message="Todos fetched successfully",
                data=paginated_data
            ),
            status=status.HTTP_200_OK
        )

    # ========================= RETRIEVE =========================
    def retrieve(self, request):
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

        todo = Todo.get_one(todo_id)
        if not todo:
            return Response(
                Utils.error_response(
                    message="Todo not found",
                    error=f"id {todo_id} does not exist"
                ),
                status=status.HTTP_200_OK
            )

        data = TodoDetailResponseSerializer.serialize(todo)

        return Response(
            Utils.success_response(
                message="Data fetched successfully",
                data=data
            ),
            status=status.HTTP_200_OK
        )

    # ========================= UPDATE =========================
    def update(self, request):
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

        serializer = (
            UpdateTodoSerializer(data=request.data)
            if request.method == "PUT"
            else PartialUpdateTodoSerializer(data=request.data, partial=True)
        )

        validation = Utils.validate(serializer)
        if validation is not True:
            return validation

        todo = Todo.update(todo_id, **serializer.validated_data)
        if not todo:
            return Response(
                Utils.error_response(
                    message="Todo not found",
                    error=f"id {todo_id} does not exist"
                ),
                status=status.HTTP_200_OK
            )

        data = TodoDetailResponseSerializer.serialize(todo)

        return Response(
            Utils.success_response(
                message="Todo updated successfully",
                data=data
            ),
            status=status.HTTP_200_OK
        )

    # ========================= DELETE =========================
    def delete(self, request):
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

        success = Todo.delete_one(todo_id)
        if not success:
            return Response(
                Utils.error_response(
                    message="Todo not found",
                    error=f"id {todo_id} does not exist"
                ),
                status=status.HTTP_200_OK
            )

        return Response(
            Utils.success_response(
                message="Todo deleted successfully"
            ),
            status=status.HTTP_200_OK
        )
