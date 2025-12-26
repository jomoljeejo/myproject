from django.db import models


class Music(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    album = models.CharField(max_length=255, blank=True, null=True)
    genre = models.CharField(max_length=100, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "music"

    def __str__(self):
        return f"{self.title} - {self.artist}"


    @staticmethod
    def create(**data):
        return Music.objects.create(**data)


    @staticmethod
    def get_all():
        return Music.objects.filter(is_active=True).order_by("-id")


    @staticmethod
    def get_one(music_id: int):
        return Music.objects.filter(id=music_id, is_active=True).first()


    @staticmethod
    def update(music_id: int, **data):
        music = Music.objects.filter(id=music_id, is_active=True).first()
        if not music:
            return None

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
