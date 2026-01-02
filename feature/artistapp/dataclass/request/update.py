from dataclasses import dataclass
from typing import Optional

@dataclass
class UpdateArtistRequest:
    tableName: Optional[str] = None
    country: Optional[str] = None

    class Meta:
        table_name = "artistapp"
