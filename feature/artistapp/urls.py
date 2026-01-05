from django.urls import path
from feature.artistapp.controller import ArtistController

urlpatterns = [
    path("create/", ArtistController.create, name="create_artist"),
    path("get_all/", ArtistController.get_all, name="list_artist"),
    path("get/", ArtistController.get, name="get_artist"),
    path("update/", ArtistController.update, name="update_artist"),
    path("delete/", ArtistController.delete, name="delete_artist"),
]
