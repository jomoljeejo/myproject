from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status

from feature.todoapp.model.model import Todo
from feature.common.utilities import Utils


class TodoView:


    def create(self, data: dict):
        todo = Todo.objects.create(
            title=data["title"],
            description=data.get("description", "")
        )

        return Response(
            Utils.success_response(
                message="Todo created successfully",
                data={"id": todo.id}
            ),
            status=status.HTTP_201_CREATED
        )

    def list_todo(self, data: dict):
        page_num = data["page_num"]
        limit = data["limit"]
        search = data.get("search")

        queryset = Todo.objects.all().order_by("-id")

        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) |
                Q(description__icontains=search)
            )

        paginator = Paginator(queryset, limit)
        page = paginator.get_page(page_num)

        items = [
            {
                "id": todo.id,
                "title": todo.title,
                "description": todo.description,
                "is_done": todo.is_done
            }
            for todo in page
        ]

        return Response(
            Utils.success_response(
                message="Todo list fetched successfully",
                data={
                    "items": items,
                    "total": paginator.count,
                    "page": page_num,
                    "limit": limit
                }
            ),
            status=status.HTTP_200_OK
        )


    def retrieve(self, data: dict):
        todo = get_object_or_404(Todo, id=data["id"])

        return Response(
            Utils.success_response(
                message="Todo fetched successfully",
                data={
                    "id": todo.id,
                    "title": todo.title,
                    "description": todo.description,
                    "is_done": todo.is_done
                }
            ),
            status=status.HTTP_200_OK
        )


    def update(self, data: dict):
        todo_id = data["id"]
        todo = get_object_or_404(Todo, id=todo_id)

        if "title" in data:
            todo.title = data["title"]
        if "description" in data:
            todo.description = data["description"]
        if "is_done" in data:
            todo.is_done = data["is_done"]

        todo.save()

        return Response(
            Utils.success_response(
                message="Todo updated successfully"
            ),
            status=status.HTTP_200_OK
        )

    def delete(self, data: dict):
        todo = get_object_or_404(Todo, id=data["id"])
        todo.delete()

        return Response(
            Utils.success_response(
                message="Todo deleted successfully"
            ),
            status=status.HTTP_200_OK
        )
