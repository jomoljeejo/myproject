class MusicListResponseSerializer:

    @staticmethod
    def serialize(music):
        return {
            "tableCode": f"MUSIC-{music.id}",
            "title": music.title,
            "artist": music.artist.name if music.artist else None,
            "album": music.album,
            "genre": music.genre,
        }
