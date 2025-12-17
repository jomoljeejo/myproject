from rest_framework.decorators import api_view
from project.feature.musicapp import views


@api_view(["POST"])
def create(request):
    return views.create_music(request)


@api_view(["GET"])
def get_all(request):
    return views.list_music(request)


@api_view(["GET"])
def get(request):
    return views.retrieve_music(request)


@api_view(["PUT", "PATCH"])
def update(request):
    return views.update_music(request)


@api_view(["DELETE"])
def delete(request):
    return views.delete_music(request)
