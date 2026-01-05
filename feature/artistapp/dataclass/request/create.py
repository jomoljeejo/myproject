from dataclasses import dataclass
from typing import Optional

@dataclass
class CreateArtistRequest:
    tableName: str
    country: Optional[str] = None


