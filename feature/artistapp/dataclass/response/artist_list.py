from dataclasses import dataclass
from typing import List
from feature.artistapp.dataclass.response.artist_detail import ArtistDetailResponse

@dataclass
class ArtistListResponse:
    data: List[ArtistDetailResponse]

    class Meta:
        table_name = "artistapp"
