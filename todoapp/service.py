# todoapp/services.py
from typing import List
from django.core.exceptions import ObjectDoesNotExist

from todoapp.model.model import Todo

from todoapp.dataclass.request.create import TodoCreateDTO
from todoapp.dataclass.request.update import TodoUpdateDTO
from todoapp.dataclass.request.partial_update import TodoPartialUpdateDTO
from todoapp.dataclass.request.delete import TodoDeleteDTO
from todoapp.dataclass.request.retrieve import TodoRetrieveDTO
from todoapp.dataclass.request.list import TodoListQueryDTO

from todoapp.dataclass.response.todo_response import TodoResponseDTO
from todoapp.dataclass.response.todo_list_response import TodoListResponseDTO

def _to_dto(todo: Todo) -> TodoResponseDTO:
    return TodoResponseDTO(
        id=todo.id,
        title=todo.title,
        description=todo.description or "",
        is_done=todo.is_done,
        created_at=todo.created_at,
        updated_at=todo.updated_at,
    )

def create_todo(dto: TodoCreateDTO) -> TodoResponseDTO:
    todo = Todo.objects.create(title=dto.title, description=dto.description or "", is_done=dto.is_done)
    return _to_dto(todo)

def update_todo(dto: TodoUpdateDTO) -> TodoResponseDTO:
    todo = Todo.objects.get(pk=dto.id)
    if dto.title is not None:
        todo.title = dto.title
    if dto.description is not None:
        todo.description = dto.description
    if dto.is_done is not None:
        todo.is_done = dto.is_done
    todo.save()
    return _to_dto(todo)

def partial_update_todo(dto: TodoPartialUpdateDTO) -> TodoResponseDTO:
    return update_todo(TodoUpdateDTO(id=dto.id, title=dto.title, description=dto.description, is_done=dto.is_done))

def delete_todo(dto: TodoDeleteDTO) -> bool:
    deleted, _ = Todo.objects.filter(pk=dto.id).delete()
    return deleted > 0

def retrieve_todo(dto: TodoRetrieveDTO) -> TodoResponseDTO:
    todo = Todo.objects.get(pk=dto.id)
    return _to_dto(todo)

def list_todos(dto: TodoListQueryDTO) -> TodoListResponseDTO:
    qs = Todo.objects.all().order_by("-created_at")
    if dto.search:
        qs = qs.filter(title__icontains=dto.search)
    if dto.is_done is not None:
        qs = qs.filter(is_done=dto.is_done)
    total = qs.count()
    offset = dto.offset or 0
    limit = dto.limit or 100
    items = [_to_dto(t) for t in qs[offset: offset + limit]]
    return TodoListResponseDTO(items=items, total=total)
