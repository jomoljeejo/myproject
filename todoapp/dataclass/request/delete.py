from dataclasses import dataclass
from typing import List

@dataclass
class TodoDeleteDTO:
    ids: List[int]

    class Meta:
        table_name = "todo"
