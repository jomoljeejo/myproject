from .music_detail import MusicDetailResponseSerializer


class MusicListResponseSerializer:

    @staticmethod
    def serialize(queryset):
        return [
            MusicDetailResponseSerializer.serialize(obj)
            for obj in queryset
        ]
