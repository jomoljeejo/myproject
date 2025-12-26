from dataclasses import dataclass


@dataclass
class ListMusicRequest:
    page_num: int = 1
    limit: int = 10

    class Meta:
        table_name = "music"
