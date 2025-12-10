from dataclasses import dataclass
from typing import Optional

@dataclass
class TodoUpdateDTO:
    id: int
    title: Optional[str] = None
    description: Optional[str] = None
    is_done: Optional[bool] = None
