from dataclasses import dataclass

@dataclass
class TodoRetrieveDTO:
    id: int

    class Meta:
        table_name = "todo"
