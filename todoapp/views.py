# todoapp/views.py
from django.db import transaction
from rest_framework.response import Response
from rest_framework import status
from django.core.paginator import Paginator
from django.db.models import Q

from todoapp.model.model import Todo
from todoapp.serializer.response.todo_detail import TodoResponseSerializer
from todoapp.serializer.response.todo_list import TodoListItemSerializer


class TodoView:

    def __init__(self):
        self.data_created = "Todo created successfully."
        self.data_updated = "Todo updated successfully."
        self.data_deleted = "Todo(s) deleted successfully."
        self.data_fetched = "Todo fetched successfully."
        self.multi_data_fetched = "Todos fetched successfully."

    # ----------------------------- CREATE -----------------------------
    def create_extract(self, params, token_payload):
        with transaction.atomic():
            todo = Todo.objects.create(
                title=params.title,
                description=params.description,
                is_done=params.is_done
            )

        return Response({
            "success": True,
            "message": self.data_created,
            "data": TodoResponseSerializer(todo).data
        }, status=status.HTTP_201_CREATED)

    # ----------------------------- RETRIEVE -----------------------------
    def get_extract(self, params, token_payload):
        try:
            todo = Todo.objects.get(id=params.id)
        except Todo.DoesNotExist:
            return Response({"success": False, "message": "Todo not found"}, status=404)

        return Response({
            "success": True,
            "message": self.data_fetched,
            "data": TodoResponseSerializer(todo).data
        })

    # ----------------------------- LIST -----------------------------
    def get_all_extract(self, params, token_payload):

        qs = Todo.objects.all().order_by("-created_at")

        if params.search:
            qs = qs.filter(
                Q(title__icontains=params.search) |
                Q(description__icontains=params.search)
            )

        paginator = Paginator(qs, params.limit)
        page = paginator.page(params.page_num)

        items = TodoListItemSerializer(page.object_list, many=True).data

        return Response({
            "success": True,
            "message": self.multi_data_fetched,
            "data": {
                "meta": {
                    "page_num": params.page_num,
                    "limit": params.limit,
                    "total": paginator.count,
                    "total_pages": paginator.num_pages
                },
                "items": items
            }
        })

    # ----------------------------- UPDATE (PUT/PATCH) -----------------------------
    def update_extract(self, params, token_payload):
        try:
            todo = Todo.objects.get(id=params.id)
        except Todo.DoesNotExist:
            return Response({"success": False, "message": "Todo not found"}, status=404)

        update_fields = {}

        if hasattr(params, "title"):
            update_fields["title"] = params.title

        if hasattr(params, "description"):
            update_fields["description"] = params.description

        if hasattr(params, "is_done"):
            update_fields["is_done"] = params.is_done

        for k, v in update_fields.items():
            setattr(todo, k, v)

        todo.save()

        return Response({
            "success": True,
            "message": self.data_updated,
            "data": TodoResponseSerializer(todo).data
        })

    # ----------------------------- DELETE MANY -----------------------------
    def delete_many_extract(self, params, token_payload):
        ids = params.ids

        deleted, _ = Todo.objects.filter(id__in=ids).delete()

        return Response({
            "success": True,
            "message": self.data_deleted,
            "data": {"deleted_count": deleted}
        })
