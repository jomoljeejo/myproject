from rest_framework.decorators import api_view
from rest_framework.request import Request

from feature.artistapp.views import ArtistView
from feature.artistapp.serializer.request.create import CreateArtistSerializer
from feature.artistapp.serializer.request.list import ListArtistRequestSerializer
from feature.common.utilities import Utils


class ArtistController:
    view = ArtistView()

    @staticmethod
    @api_view(["POST"])
    def create(request: Request):
        serializer = CreateArtistSerializer(data=request.data)
        validation = Utils.validate(serializer)
        if validation is not True:
            return validation

        request.validated_data = serializer.validated_data
        return ArtistController.view.create(request)

    @staticmethod
    @api_view(["GET"])
    def get_all(request: Request):
        serializer = ListArtistRequestSerializer(data=request.query_params)
        validation = Utils.validate(serializer)
        if validation is not True:
            return validation

        request.validated_data = serializer.validated_data
        return ArtistController.view.list_artist(request)
