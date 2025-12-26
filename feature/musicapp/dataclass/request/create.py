from dataclasses import dataclass
from typing import Optional


@dataclass
class CreateMusicRequest:
    tableName: str
    artist: str
    album: Optional[str] = None
    genre: Optional[str] = None

    class Meta:
        table_name = "music"
