from dataclasses import dataclass
from typing import Optional

@dataclass
class PartialUpdateMusicRequest:
    title: Optional[str] = None
    artist: Optional[str] = None
    album: Optional[str] = None
    genre: Optional[str] = None
