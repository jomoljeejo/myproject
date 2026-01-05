from dataclasses import dataclass
from typing import Optional

@dataclass
class UpdateArtistRequest:
    artist_id: int
    name: str
    country: Optional[str] = None
