class MusicDetailResponseSerializer:

    @staticmethod
    def serialize(obj):
        return {
            "tableName": obj.title,
            "tableCode": f"MUSIC-{obj.id}",
            "artist": obj.artist,
            "album": obj.album,
            "genre": obj.genre,
            "createdDateTime": obj.created_at,
            "isActive": obj.is_active,
            "createdBy": "System",
            "createdBranch": None,
            "createdByCode": "SYS",
            "createdBranchCode": None,
        }
