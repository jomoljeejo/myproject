from dataclasses import dataclass
from typing import Optional


@dataclass
class PartialUpdateMusicRequest:
    tableName: Optional[str] = None
    artist: Optional[str] = None
    album: Optional[str] = None
    genre: Optional[str] = None

    class Meta:
        table_name = "music"
