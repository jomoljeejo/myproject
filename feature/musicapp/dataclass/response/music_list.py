from dataclasses import dataclass
from typing import List
from feature.musicapp.dataclass.response.music_detail import MusicDetailResponse


@dataclass
class MusicListResponse:
    data: List[MusicDetailResponse]

    class Meta:
        table_name = "music"
