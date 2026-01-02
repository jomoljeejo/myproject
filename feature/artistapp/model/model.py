from django.db import models
from django.utils import timezone


class Artist(models.Model):
    artist_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "artist"

    def __str__(self):
        return self.name


    @staticmethod
    def get_by_name(name: str):
        return Artist.objects.filter(name=name, is_active=True).first()

    @staticmethod
    def get_all():
        return Artist.objects.filter(is_active=True).order_by("-artist_id")

    @staticmethod
    def deactivate(artist_id: int):
        return Artist.objects.filter(
            artist_id=artist_id
        ).update(is_active=False)
