# todoapp/controller.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# request serializers
from todoapp.serializer.request import (
    CreateTodoSerializer,
    RetrieveTodoSerializer,
    ListTodoRequestSerializer,
    UpdateTodoSerializer,
    PartialUpdateTodoSerializer,
    TodoDeleteRequestSerializer,
)

# DTOs
from todoapp.dataclass.request.create import TodoCreateDTO
from todoapp.dataclass.request.update import TodoUpdateDTO
from todoapp.dataclass.request.partial_update import TodoPartialUpdateDTO
from todoapp.dataclass.request.retrieve import TodoRetrieveDTO
from todoapp.dataclass.request.list import TodoListDTO
from todoapp.dataclass.request.delete import TodoDeleteDTO

# service layer
from todoapp.views import TodoView


def _get_token_payload(request):
    """Support token from middleware."""
    return getattr(request, "token_payload", None) or request.META.get("token_payload")


# =====================================================================================
# CREATE
# =====================================================================================
@api_view(["POST"])
def todo_create(request):
    serializer = CreateTodoSerializer(data=request.data)

    if not serializer.is_valid():
        return Response(serializer.errors, status=400)

    v = serializer.validated_data

    dto = TodoCreateDTO(
        title=v["title"],
        description=v.get("description"),
        # serializer uses "completed", but your DTO uses "is_done"
        is_done=v.get("completed", False),
    )

    view = TodoView()
    return view.create_extract(dto, _get_token_payload(request))


# =====================================================================================
# RETRIEVE
# =====================================================================================
@api_view(["GET"])
def todo_retrieve(request, pk):
    serializer = RetrieveTodoSerializer(data={"id": pk})

    if not serializer.is_valid():
        return Response(serializer.errors, status=400)

    dto = TodoRetrieveDTO(id=int(pk))

    view = TodoView()
    return view.get_extract(dto, _get_token_payload(request))


# =====================================================================================
# LIST
# =====================================================================================
@api_view(["GET"])
def todo_list(request):
    serializer = ListTodoRequestSerializer(data=request.query_params)

    if not serializer.is_valid():
        return Response(serializer.errors, status=400)

    v = serializer.validated_data

    dto = TodoListDTO(
        page_num=v.get("page_num", 1),
        limit=v.get("limit", 10),
        search=v.get("search"),
    )

    view = TodoView()
    return view.get_all_extract(dto, _get_token_payload(request))


# =====================================================================================
# UPDATE (PUT)
# =====================================================================================
@api_view(["PUT"])
def todo_update(request, pk):
    serializer = UpdateTodoSerializer(data=request.data)

    if not serializer.is_valid():
        return Response(serializer.errors, status=400)

    v = serializer.validated_data

    dto = TodoUpdateDTO(
        id=int(pk),
        title=v.get("title"),
        description=v.get("description"),
        is_done=v.get("completed"),
    )

    view = TodoView()
    return view.update_extract(dto, _get_token_payload(request))


# =====================================================================================
# PARTIAL UPDATE (PATCH)
# =====================================================================================
@api_view(["PATCH"])
def todo_partial_update(request, pk):
    serializer = PartialUpdateTodoSerializer(data=request.data)

    if not serializer.is_valid():
        return Response(serializer.errors, status=400)

    v = serializer.validated_data

    dto = TodoPartialUpdateDTO(
        id=int(pk),
        title=v.get("title"),
        description=v.get("description"),
        is_done=v.get("completed"),
    )

    view = TodoView()
    return view.update_extract(dto, _get_token_payload(request))


# =====================================================================================
# DELETE MANY
# =====================================================================================
@api_view(["POST"])
def todo_delete_many(request):
    serializer = TodoDeleteRequestSerializer(data=request.data)

    if not serializer.is_valid():
        return Response(serializer.errors, status=400)

    v = serializer.validated_data

    dto = TodoDeleteDTO(
        ids=v["ids"]  # list of ints
    )

    view = TodoView()
    return view.delete_many_extract(dto, _get_token_payload(request))
