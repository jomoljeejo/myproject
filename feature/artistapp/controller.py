from rest_framework.decorators import api_view
from rest_framework.request import Request

from feature.artistapp.views import ArtistView
from feature.artistapp.serializer.request.create import CreateArtistSerializer
from feature.artistapp.serializer.request.list import ListArtistRequestSerializer
from feature.artistapp.serializer.request.retrieve import RetrieveArtistRequestSerializer
from feature.artistapp.serializer.request.update import UpdateArtistRequestSerializer
from feature.artistapp.serializer.request.delete import DeleteArtistRequestSerializer
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

        request.validated_data = serializer.save()

        return ArtistController.view.create(request)

    @staticmethod
    @api_view(["GET"])
    def get_all(request: Request):
        serializer = ListArtistRequestSerializer(data=request.query_params)
        validation = Utils.validate(serializer)
        if validation is not True:
            return validation

        request.validated_data = serializer.save()

        return ArtistController.view.list_artist(request)


    @staticmethod
    @api_view(["GET"])
    def get(request: Request):
        serializer = RetrieveArtistRequestSerializer(data=request.query_params)
        validation = Utils.validate(serializer)
        if validation is not True:
            return validation

        request.validated_data = serializer.save()

        return ArtistController.view.retrieve(request)


    @staticmethod
    @api_view(["PUT"])
    def update(request: Request):
        serializer = UpdateArtistRequestSerializer(data=request.data)
        validation = Utils.validate(serializer)
        if validation is not True:
            return validation

        request.validated_data = serializer.save()

        return ArtistController.view.update(request)


    @staticmethod
    @api_view(["DELETE"])
    def delete(request: Request):
        serializer = DeleteArtistRequestSerializer(data=request.data)
        validation = Utils.validate(serializer)
        if validation is not True:
            return validation

        request.validated_data = serializer.save()

        return ArtistController.view.delete(request)
