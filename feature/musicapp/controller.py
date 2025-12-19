from rest_framework.decorators import api_view
from rest_framework.request import Request

from feature.musicapp.views import MusicView
from feature.musicapp.serializer.request.create import CreateMusicSerializer
from feature.musicapp.serializer.request.update import UpdateMusicSerializer
from feature.musicapp.serializer.request.partial_update import (
    PartialUpdateMusicSerializer
)
from feature.common.utilities import Utils


class MusicController:
    view = MusicView()

    @staticmethod
    @api_view(["POST"])
    def create(request: Request):
        serializer = CreateMusicSerializer(data=request.data)
        validation = Utils.validate(serializer)
        if validation is not True:
            return validation

        request.validated_data = serializer.validated_data
        return MusicController.view.create(request)


    @staticmethod
    @api_view(["GET"])
    def get_all(request: Request):
        return MusicController.view.list_music(request)


    @staticmethod
    @api_view(["GET"])
    def get(request: Request):
        return MusicController.view.retrieve(request)


    @staticmethod
    @api_view(["PUT", "PATCH"])
    def update(request: Request):
        serializer = (
            UpdateMusicSerializer(data=request.data)
            if request.method == "PUT"
            else PartialUpdateMusicSerializer(
                data=request.data, partial=True
            )
        )

        validation = Utils.validate(serializer)
        if validation is not True:
            return validation

        request.validated_data = serializer.validated_data
        return MusicController.view.update(request)


    @staticmethod
    @api_view(["DELETE"])
    def delete(request: Request):
        return MusicController.view.delete(request)
