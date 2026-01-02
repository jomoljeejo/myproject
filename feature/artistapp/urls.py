from django.urls import path
from feature.artistapp.controller import ArtistController

urlpatterns = [
    path("create/", ArtistController.create, name="create_artist"),
    path("get_all/", ArtistController.get_all, name="list_artist"),
]
