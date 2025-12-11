# todoapp/controller.py
from typing import Any, Dict, List

from django.shortcuts import get_object_or_404
from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from todoapp.model.model import Todo

# request serializers (your existing request serializers)
from todoapp.serializer.request import (
    CreateTodoSerializer,
    RetrieveTodoSerializer,
    ListTodoRequestSerializer,
    UpdateTodoSerializer,
    PartialUpdateTodoSerializer,
    TodoDeleteRequestSerializer,
)


def _get_token_payload(request):
    """Support token from middleware (keep existing behaviour)."""
    return getattr(request, "token_payload", None) or request.META.get("token_payload")


def _serialize_todo(todo: Todo) -> Dict[str, Any]:
    """Return a JSON-serializable dict for a Todo instance."""
    return {
        "id": todo.id,
        "title": todo.title,
        "description": todo.description,
        "is_done": todo.is_done,
        "created_at": todo.created_at.isoformat() if todo.created_at else None,
        "updated_at": todo.updated_at.isoformat() if todo.updated_at else None,
    }


def _wrap(success: bool, message: str, data, code=status.HTTP_200_OK):
    return Response({"success": success, "message": message, "data": data}, status=code)


# ======================
# CREATE
# ======================
@api_view(["POST"])
def todo_create(request):
    serializer = CreateTodoSerializer(data=request.data)
    if not serializer.is_valid():
        return _wrap(False, "Validation failed.", serializer.errors, code=status.HTTP_400_BAD_REQUEST)

    v = serializer.validated_data

    # Accept both 'completed' or 'is_done' depending on your client/serializer
    is_done = v.get("completed")
    if is_done is None:
        is_done = v.get("is_done", False)

    todo = Todo.objects.create(
        title=v["title"],
        description=v.get("description"),
        is_done=bool(is_done),
    )

    return _wrap(True, "Todo created successfully.", _serialize_todo(todo), code=status.HTTP_201_CREATED)


# ======================
# RETRIEVE
# ======================
@api_view(["GET"])
def todo_retrieve(request, pk):
    # validate pk via your serializer
    serializer = RetrieveTodoSerializer(data={"id": pk})
    if not serializer.is_valid():
        return _wrap(False, "Validation failed.", serializer.errors, code=status.HTTP_400_BAD_REQUEST)

    try:
        todo = Todo.objects.get(pk=int(pk))
    except (Todo.DoesNotExist, ValueError):
        return _wrap(False, "Todo not found.", None, code=status.HTTP_404_NOT_FOUND)

    return _wrap(True, "Todo fetched successfully.", _serialize_todo(todo))


# ======================
# LIST
# ======================
@api_view(["GET"])
def todo_list(request):
    serializer = ListTodoRequestSerializer(data=request.query_params)
    if not serializer.is_valid():
        return _wrap(False, "Validation failed.", serializer.errors, code=status.HTTP_400_BAD_REQUEST)

    v = serializer.validated_data
    page_num = max(int(v.get("page_num", 1)), 1)
    limit = max(int(v.get("limit", 10)), 1)
    search = v.get("search")

    qs = Todo.objects.all().order_by("-created_at")
    if search:
        # basic search on title or description
        qs = qs.filter(Q(title__icontains=search) | Q(description__icontains=search))

    total = qs.count()
    start = (page_num - 1) * limit
    end = start + limit
    items = qs[start:end]

    data = {
        "meta": {"page_num": page_num, "limit": limit, "total": total},
        "items": [_serialize_todo(t) for t in items],
    }
    return _wrap(True, "Todos fetched successfully.", data)


# ======================
# UPDATE (PUT)
# ======================
@api_view(["PUT"])
def todo_update(request, pk):
    serializer = UpdateTodoSerializer(data=request.data)
    if not serializer.is_valid():
        return _wrap(False, "Validation failed.", serializer.errors, code=status.HTTP_400_BAD_REQUEST)

    v = serializer.validated_data

    try:
        todo = Todo.objects.get(pk=int(pk))
    except (Todo.DoesNotExist, ValueError):
        return _wrap(False, "Todo not found.", None, code=status.HTTP_404_NOT_FOUND)

    # For PUT treat missing fields as explicit intent to set to None or default.
    # Use provided keys to update. You can adjust to require all fields if your UpdateTodoSerializer enforces that.
    title = v.get("title")
    description = v.get("description")
    is_done = v.get("completed")
    if is_done is None:
        is_done = v.get("is_done")

    if title is not None:
        todo.title = title
    todo.description = description  # could be None or blank
    if is_done is not None:
        todo.is_done = bool(is_done)

    todo.save()
    return _wrap(True, "Todo updated successfully.", _serialize_todo(todo))


# ======================
# PARTIAL UPDATE (PATCH)
# ======================
@api_view(["PATCH"])
def todo_partial_update(request, pk):
    serializer = PartialUpdateTodoSerializer(data=request.data)
    if not serializer.is_valid():
        return _wrap(False, "Validation failed.", serializer.errors, code=status.HTTP_400_BAD_REQUEST)

    v = serializer.validated_data

    try:
        todo = Todo.objects.get(pk=int(pk))
    except (Todo.DoesNotExist, ValueError):
        return _wrap(False, "Todo not found.", None, code=status.HTTP_404_NOT_FOUND)

    # Update only provided fields
    if "title" in v:
        todo.title = v.get("title")
    if "description" in v:
        todo.description = v.get("description")
    if "completed" in v:
        todo.is_done = bool(v.get("completed"))
    elif "is_done" in v:
        todo.is_done = bool(v.get("is_done"))

    todo.save()
    return _wrap(True, "Todo partially updated successfully.", _serialize_todo(todo))


# ======================
# DELETE MANY
# ======================
@api_view(["POST"])
def todo_delete_many(request):
    serializer = TodoDeleteRequestSerializer(data=request.data)
    if not serializer.is_valid():
        return _wrap(False, "Validation failed.", serializer.errors, code=status.HTTP_400_BAD_REQUEST)

    v = serializer.validated_data
    ids = v.get("ids", [])
    if not isinstance(ids, (list, tuple)):
        return _wrap(False, "ids must be a list of integers.", None, code=status.HTTP_400_BAD_REQUEST)

    # Filter and delete only existing ids
    qs = Todo.objects.filter(id__in=ids)
    deleted_count, _ = qs.delete()

    return _wrap(True, f"Deleted {deleted_count} todos.", {"deleted_count": deleted_count})
