from dataclasses import dataclass

@dataclass
class ListArtistRequest:
    page_num: int = 1
    limit: int = 10

    class Meta:
        table_name = "artistapp"
