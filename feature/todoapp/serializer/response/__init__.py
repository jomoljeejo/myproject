# todoapp/serializer/response/__init__.py
# Re-export response serializers using the names other modules expect.

# todo_detail.py defines TodoResponseSerializer (non-ModelSerializer).
# Alias it here so imports that expect TodoDetailSerializer continue to work.
from .todo_detail import TodoDetailResponseSerializer as TodoDetailSerializer

from .todo_list import TodoListItemSerializer
from .utils import PaginationSerializer

__all__ = [
    "TodoDetailSerializer",
    "TodoListItemSerializer",
    "PaginationSerializer",
]


