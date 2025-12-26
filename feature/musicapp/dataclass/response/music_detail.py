from dataclasses import dataclass
from typing import Optional


@dataclass
class MusicDetailResponse:
    tableName: str
    tableCode: str
    artist: str
    album: Optional[str]
    genre: Optional[str]
    createdDateTime: str
    isActive: bool
    createdBy: Optional[str]
    createdBranch: Optional[str]
    createdByCode: Optional[str]
    createdBranchCode: Optional[str]

    class Meta:
        table_name = "music"
