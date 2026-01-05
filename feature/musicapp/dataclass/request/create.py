from dataclasses import dataclass
from typing import Optional

@dataclass
class CreateMusicRequest:
    title: str
    artist: str
    album: Optional[str] = None
    duration: Optional[int] = None
