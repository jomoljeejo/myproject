from django.db import models
from feature.artistapp.model.model import Artist


class Music(models.Model):
    title = models.CharField(max_length=255)


    artist = models.ForeignKey(
        Artist,
        on_delete=models.DO_NOTHING,
        related_name="music_set"
    )

    album = models.CharField(max_length=255, blank=True, null=True)
    genre = models.CharField(max_length=100, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "musicapp_music"

    def __str__(self):
        return f"{self.title} - {self.artist.name}"




    @staticmethod
    def create(**data):
        artist_name = data.pop("artist")

        artist_obj = Artist.get_by_name(artist_name)
        if not artist_obj:
            raise ValueError("Artist not found")

        return Music.objects.create(
            artist=artist_obj,
            **data
        )

    @staticmethod
    def get_all():
        return Music.objects.select_related("artist").filter(
            is_active=True
        ).order_by("-id")

    @staticmethod
    def get_one(music_id: int):
        return Music.objects.select_related("artist").filter(
            id=music_id,
            is_active=True
        ).first()

    @staticmethod
    def update(music_id: int, **data):
        music = Music.objects.filter(id=music_id, is_active=True).first()
        if not music:
            return None

        if "artist" in data:
            artist_name = data.pop("artist")
            artist_obj = Artist.get_by_name(artist_name)
            if not artist_obj:
                raise ValueError("Artist not found")
            music.artist = artist_obj

        for field, value in data.items():
            setattr(music, field, value)

        music.save()
        return music

    @staticmethod
    def delete_one(music_id: int):
        music = Music.objects.filter(id=music_id, is_active=True).first()
        if not music:
            return False

        music.is_active = False
        music.save()
        return True
