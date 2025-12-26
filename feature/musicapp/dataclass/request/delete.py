from dataclasses import dataclass


@dataclass
class DeleteMusicRequest:
    tableCode: str

    class Meta:
        table_name = "music"
