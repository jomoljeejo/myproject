from dataclasses import dataclass
from typing import Optional

@dataclass
class TodoListQueryDTO:
    search: Optional[str] = None
    is_done: Optional[bool] = None
    limit: int = 100
    offset: int = 0

