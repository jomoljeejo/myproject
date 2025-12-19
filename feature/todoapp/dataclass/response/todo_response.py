from dataclasses import dataclass
from datetime import datetime

@dataclass
class TodoResponseDTO:
    id: int
    title: str
    description: str
    is_done: bool
    created_at: datetime
    updated_at: datetime
