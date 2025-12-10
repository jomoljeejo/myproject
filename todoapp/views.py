from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from todoapp.serializer.request.create import TodoCreateRequestSerializer, to_create_dto
from todoapp.serializer.request.update import TodoUpdateRequestSerializer, to_update_dto
from todoapp.serializer.request.partial_update import TodoPartialUpdateRequestSerializer, to_partial_update_dto
from todoapp.serializer.request.delete import TodoDeleteRequestSerializer, to_delete_dto
from todoapp.serializer.request.retrieve import TodoRetrieveRequestSerializer, to_retrieve_dto
from todoapp.serializer.request.list import TodoListRequestSerializer, to_list_dto

from todoapp.serializer.response import TodoResponseSerializer, TodoListResponseSerializer, dataclass_to_primitive

from . import service


# CREATE
@api_view(['POST'])
def todo_create(request):
    ser = TodoCreateRequestSerializer(data=request.data)
    ser.is_valid(raise_exception=True)
    dto = to_create_dto(ser)
    resp_dto = service.create_todo(dto)
    payload = dataclass_to_primitive(resp_dto)
    resp_ser = TodoResponseSerializer(payload)
    return Response(resp_ser.data, status=status.HTTP_201_CREATED)

# LIST
@api_view(['GET'])
def todo_list(request):
    ser = TodoListRequestSerializer(data=request.query_params)
    ser.is_valid(raise_exception=True)
    qdto = to_list_dto(ser)
    list_resp = service.list_todos(qdto)
    items = [dataclass_to_primitive(i) for i in list_resp.items]
    payload = {"items": items, "total": list_resp.total}
    resp_ser = TodoListResponseSerializer(payload)
    return Response(resp_ser.data, status=status.HTTP_200_OK)

# RETRIEVE
@api_view(['GET'])
def todo_retrieve(request, pk: int):
    ser = TodoRetrieveRequestSerializer(data={"id": pk})
    ser.is_valid(raise_exception=True)
    dto = to_retrieve_dto(ser)
    try:
        resp_dto = service.retrieve_todo(dto)
    except Exception:
        return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)
    payload = dataclass_to_primitive(resp_dto)
    resp_ser = TodoResponseSerializer(payload)
    return Response(resp_ser.data, status=status.HTTP_200_OK)

# UPDATE (PUT)
@api_view(['PUT'])
def todo_update(request, pk: int):
    body = {**request.data, "id": pk}
    ser = TodoUpdateRequestSerializer(data=body)
    ser.is_valid(raise_exception=True)
    dto = to_update_dto(ser)
    try:
        resp_dto = service.update_todo(dto)
    except Exception:
        return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)
    payload = dataclass_to_primitive(resp_dto)
    resp_ser = TodoResponseSerializer(payload)
    return Response(resp_ser.data, status=status.HTTP_200_OK)

# PARTIAL (PATCH)
@api_view(['PATCH'])
def todo_partial_update(request, pk: int):
    body = {**request.data, "id": pk}
    ser = TodoPartialUpdateRequestSerializer(data=body)
    ser.is_valid(raise_exception=True)
    dto = to_partial_update_dto(ser)
    try:
        resp_dto = service.partial_update_todo(dto)
    except Exception:
        return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)
    payload = dataclass_to_primitive(resp_dto)
    resp_ser = TodoResponseSerializer(payload)
    return Response(resp_ser.data, status=status.HTTP_200_OK)

# DELETE
@api_view(['DELETE'])
def todo_delete(request, pk: int):
    ser = TodoDeleteRequestSerializer(data={"id": pk})
    ser.is_valid(raise_exception=True)
    dto = to_delete_dto(ser)
    ok = service.delete_todo(dto)
    if ok:
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)
