from dataclasses import dataclass
from typing import Optional

@dataclass
class TodoListDTO:
    page_num: int
    limit: int
    search: Optional[str] = None

    class Meta:
        table_name = "todo"
