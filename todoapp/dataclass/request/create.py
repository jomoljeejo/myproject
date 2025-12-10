from dataclasses import dataclass
from typing import Optional

@dataclass
class TodoCreateDTO:
    title: str
    description: Optional[str] = ""
    is_done: bool = False

