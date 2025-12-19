from django.urls import path
from feature.musicapp.controller import MusicController

urlpatterns = [
    path("create/", MusicController.create),
    path("get_all/", MusicController.get_all),
    path("get/", MusicController.get),
    path("update/", MusicController.update),
    path("delete/", MusicController.delete),
]

