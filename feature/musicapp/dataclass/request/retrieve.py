from dataclasses import dataclass


@dataclass
class RetrieveMusicRequest:
    tableCode: str

    class Meta:
        table_name = "music"
