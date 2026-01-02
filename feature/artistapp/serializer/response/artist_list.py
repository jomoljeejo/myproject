from .artist_detail import ArtistDetailResponseSerializer


class ArtistListResponseSerializer:

    @staticmethod
    def serialize(queryset):
        return [
            ArtistDetailResponseSerializer.serialize(obj)
            for obj in queryset
        ]
