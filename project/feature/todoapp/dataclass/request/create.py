from dataclasses import dataclass
from typing import Optional

@dataclass
class TodoCreateDTO:
    title: str
    description: Optional[str] = None
    is_done: bool = False

    class Meta:
        table_name = "todo"
