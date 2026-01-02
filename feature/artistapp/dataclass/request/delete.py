from dataclasses import dataclass

@dataclass
class DeleteArtistRequest:
    tableCode: str

    class Meta:
        table_name = "artistapp"
