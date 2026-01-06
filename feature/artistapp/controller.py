from drf_spectacular.utils import extend_schema
from rest_framework.decorators import api_view
from rest_framework.request import Request

from feature.artistapp.views import ArtistView
from feature.artistapp.serializer.request.create import CreateArtistSerializer
from feature.artistapp.serializer.request.list import ListArtistRequestSerializer
from feature.artistapp.serializer.request.retrieve import RetrieveArtistRequestSerializer
from feature.artistapp.serializer.request.update import UpdateArtistRequestSerializer
from feature.artistapp.serializer.request.delete import DeleteArtistRequestSerializer
from feature.common.utilities import Utils
from feature.common.swagger.swagger_page import SwaggerPage


class ArtistController:
    view = ArtistView()

    @extend_schema(
        description="Create a new artist",
        request=CreateArtistSerializer,
        responses=SwaggerPage.response()
    )
    @api_view(["POST"])
    def create(request: Request):
        serializer = CreateArtistSerializer(data=request.data)
        validation = Utils.validate(serializer)
        if validation is not True:
            return validation

        request.validated_data = serializer.save()
        return ArtistController.view.create(request)

    @extend_schema(
        description="Get all artists",
        parameters=SwaggerPage.list_parameters(),
        responses=SwaggerPage.response()
    )
    @api_view(["GET"])
    def get_all(request: Request):
        serializer = ListArtistRequestSerializer(data=request.query_params)
        validation = Utils.validate(serializer)
        if validation is not True:
            return validation

        request.validated_data = serializer.save()
        return ArtistController.view.list_artist(request)

    @extend_schema(
        description="Get artist by id",
        responses=SwaggerPage.response()
    )
    @api_view(["GET"])
    def get(request: Request):
        serializer = RetrieveArtistRequestSerializer(data=request.query_params)
        validation = Utils.validate(serializer)
        if validation is not True:
            return validation

        request.validated_data = serializer.save()
        return ArtistController.view.retrieve(request)

    @extend_schema(
        description="Update artist",
        request=UpdateArtistRequestSerializer,
        responses=SwaggerPage.response()
    )
    @api_view(["PUT"])
    def update(request: Request):
        serializer = UpdateArtistRequestSerializer(data=request.data)
        validation = Utils.validate(serializer)
        if validation is not True:
            return validation

        request.validated_data = serializer.save()
        return ArtistController.view.update(request)

    @extend_schema(
        description="Delete artist",
        request=DeleteArtistRequestSerializer,
        responses=SwaggerPage.response()
    )
    @api_view(["DELETE"])
    def delete(request: Request):
        serializer = DeleteArtistRequestSerializer(data=request.data)
        validation = Utils.validate(serializer)
        if validation is not True:
            return validation

        request.validated_data = serializer.save()
        return ArtistController.view.delete(request)
