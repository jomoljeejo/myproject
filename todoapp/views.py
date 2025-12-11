from django.db import transaction
from django.core.paginator import Paginator
from rest_framework import status
from rest_framework.response import Response

from todoapp.dataclass.request.create import TodoCreateDTO
from todoapp.dataclass.request.retrieve import TodoRetrieveDTO
from todoapp.model.model import Todo


class TodoView:
    def __init__(self):
        self.data_created = "Todo created successfully."
        self.data_updated = "Todo updated successfully."
        self.data_deleted = "Todo(s) deleted successfully."
        self.data_fetched = "Todo fetched successfully."
        self.multi_data_fetched = "Todos fetched successfully."

    # ========================================================================
    # CREATE
    # ========================================================================
    def create_extract(self, params: TodoCreateDTO, token_payload):
        with transaction.atomic():
            Todo.create_todo(
                title=params.title,
                description=params.description,
                is_done=params.is_done      # <-- FIXED
            )

        return Response(
            {"success": True, "message": self.data_created},
            status=status.HTTP_201_CREATED
        )

    # ========================================================================
    # RETRIEVE
    # ========================================================================
    def get_extract(self, params: TodoRetrieveDTO, token_payload):
        obj = Todo.get_todo(id=params.id)

        from todoapp.serializer.response.todo_detail import TodoResponseSerializer

        return Response({
            "success": True,
            "message": self.data_fetched,
            "data": TodoResponseSerializer(obj).data     # <-- Correct response serializer
        }, status=200)

    # ========================================================================
    # LIST ALL
    # ========================================================================
    def get_all_extract(self, params, token_payload):
        all_objs = Todo.list_todos()

        paginator = Paginator(all_objs, params.limit)

        if paginator.num_pages > 0 and params.page_num > paginator.num_pages:
            return Response({"success": False, "message": "Page number exceeded"}, status=400)

        page_obj = paginator.page(params.page_num)

        from todoapp.serializer.response.todo_list import TodoListItemSerializer

        serialized_data = TodoListItemSerializer(page_obj.object_list, many=True).data

        return Response({
            "success": True,
            "message": self.multi_data_fetched,
            "data": {
                "results": serialized_data,
                "page": params.page_num,
                "total_pages": paginator.num_pages,
                "total_count": paginator.count,
            }
        }, status=200)

    # ========================================================================
    # UPDATE (PUT / PATCH)
    # ========================================================================
    def update_extract(self, params, token_payload):
        with transaction.atomic():
            update_fields = {
                k: v for k, v in {
                    "title": getattr(params, "title", None),
                    "description": getattr(params, "description", None),
                    "is_done": getattr(params, "is_done", None)   # <-- FIXED
                }.items() if v is not None
            }

            Todo.update_todo(id=params.id, fields=update_fields)

        return Response(
            {"success": True, "message": self.data_updated},
            status=200
        )

    # ========================================================================
    # DELETE
    # ========================================================================
    def delete_many_extract(self, params, token_payload):
        with transaction.atomic():
            Todo.delete_many_todos(ids=params.ids)

        return Response(
            {"success": True, "message": self.data_deleted},
            status=200
        )
