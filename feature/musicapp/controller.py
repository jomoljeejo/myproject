from rest_framework.decorators import api_view
from rest_framework.request import Request

from feature.musicapp.views import MusicView
from feature.common.utilities import Utils

from feature.musicapp.serializer.request.create import CreateMusicSerializer
from feature.musicapp.serializer.request.update import UpdateMusicSerializer
from feature.musicapp.serializer.request.partial_update import (
    PartialUpdateMusicSerializer
)
from feature.musicapp.serializer.request.retrieve import RetrieveMusicSerializer
from feature.musicapp.serializer.request.delete import DeleteMusicSerializer
from feature.musicapp.serializer.request.list import ListMusicRequestSerializer


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
        serializer = ListMusicRequestSerializer(data=request.query_params)
        validation = Utils.validate(serializer)
        if validation is not True:
            return validation

        request.validated_data = serializer.validated_data
        return MusicController.view.list_music(request)

    @staticmethod
    @api_view(["GET"])
    def get(request: Request):
        serializer = RetrieveMusicSerializer(data=request.query_params)
        validation = Utils.validate(serializer)
        if validation is not True:
            return validation

        request.validated_data = serializer.validated_data
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

        table_code = request.query_params.get("tableCode")
        if not table_code:
            return Utils.error_response("tableCode is required")

        request.validated_data = serializer.validated_data
        request.validated_data["tableCode"] = table_code

        return MusicController.view.update(request)

    @staticmethod
    @api_view(["DELETE"])
    def delete(request: Request):
        serializer = DeleteMusicSerializer(data=request.query_params)
        validation = Utils.validate(serializer)
        if validation is not True:
            return validation

        request.validated_data = serializer.validated_data
        return MusicController.view.delete(request)
