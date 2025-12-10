from dataclasses import dataclass
from typing import List, Optional
from .todo_response import TodoResponseDTO

@dataclass
class TodoListResponseDTO:
    items: List[TodoResponseDTO]
    total: Optional[int] = None
