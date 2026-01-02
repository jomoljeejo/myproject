from dataclasses import dataclass
from typing import Optional


@dataclass
class UpdateMusicRequest:
    tableName: Optional[str] = None
    artist: Optional[str] = None
    album: Optional[str] = None
    genre: Optional[str] = None


