from dataclasses import dataclass

@dataclass
class RetrieveArtistRequest:
    tableCode: str   # ARTIST-<id>

    class Meta:
        table_name = "artistapp"
