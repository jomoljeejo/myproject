from django.urls import path
from feature.musicapp.controller import MusicController

urlpatterns = [
    path("create/", MusicController.create, name="create_music"),
    path("get_all/", MusicController.get_all, name="list_music"),
    path("get/", MusicController.get, name="retrieve_music"),
    path("update/", MusicController.update, name="update_music"),
    path("delete/", MusicController.delete, name="delete_music"),
]


