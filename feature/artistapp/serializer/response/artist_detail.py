class ArtistDetailResponseSerializer:

    @staticmethod
    def serialize(obj):
        return {
            "tableName": obj.name,
            "tableCode": f"ARTIST-{obj.artist_id}",
            "country": obj.country,
            "createdDateTime": obj.created_at,
            "isActive": obj.is_active,
            "createdBy": "System",
            "createdBranch": None,
            "createdByCode": "SYS",
            "createdBranchCode": None,
        }
