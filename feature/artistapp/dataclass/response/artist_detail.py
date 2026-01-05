from dataclasses import dataclass
from typing import Optional

@dataclass
class ArtistDetailResponse:
    tableName: str
    tableCode: str
    country: Optional[str]
    createdDateTime: str
    isActive: bool
    createdBy: Optional[str]
    createdBranch: Optional[str]
    createdByCode: Optional[str]
    createdBranchCode: Optional[str]
