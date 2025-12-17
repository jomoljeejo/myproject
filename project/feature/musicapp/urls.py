from django.urls import path
from project.feature.musicapp import controller

urlpatterns = [
    path("create/", controller.create),
    path("get_all/", controller.get_all),
    path("get/", controller.get),
    path("update/", controller.update),
    path("delete/", controller.delete),
]
