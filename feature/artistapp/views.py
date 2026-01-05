from django.core.paginator import Paginator, EmptyPage
from rest_framework import status
from rest_framework.response import Response


from feature.artistapp.model.model import Artist
from feature.artistapp.serializer.response.artist_detail import (
    ArtistDetailResponseSerializer
)
from feature.common.common import Common
from feature.common.utilities import Utils


class ArtistView:


    @Common(
        response_handler=ArtistDetailResponseSerializer,
        message="Artist created successfully",
        status_code=status.HTTP_201_CREATED
    ).exception_handler
    @Common(
        response_handler=ArtistDetailResponseSerializer,
        message="Artist created successfully",
        status_code=status.HTTP_201_CREATED
    ).exception_handler
    def create(self, request):
        data = request.validated_data  # CreateArtistRequest DTO

        return Artist.create_artist(
            name=data.tableName,
            country=data.country
        )

    def list_artist(self, request):
        data = request.validated_data

        paginator = Paginator(Artist.get_all(), data.limit)

        try:
            page = paginator.page(data.page_num)
            serialized = [
                ArtistDetailResponseSerializer.serialize(obj)
                for obj in page
            ]
        except EmptyPage:
            serialized = []

        final_data = Utils.add_page_parameter(
            final_data=serialized,
            page_num=data.page_num,
            total_page=paginator.num_pages,
            total_count=paginator.count,
            present_url=request.get_full_path(),
            next_page_required=True
        )

        return Response(
            Utils.success_response(
                message="Artist list fetched successfully",
                data=final_data
            ),
            status=status.HTTP_200_OK
        )

    @Common(
        response_handler=ArtistDetailResponseSerializer,
        message="Artist fetched successfully"
    ).exception_handler
    def retrieve(self, request):
        data = request.validated_data

        artist = Artist.get_by_id(data.artist_id)
        if not artist:
            raise ValueError("Artist not found")

        return artist

    @Common(
        response_handler=ArtistDetailResponseSerializer,
        message="Artist updated successfully"
    ).exception_handler
    def update(self, request):
        data = request.validated_data

        artist = Artist.update_artist(
            artist_id=data.artist_id,
            name=data.name,
            country=data.country
        )

        if not artist:
            raise ValueError("Artist not found")

        return artist

    @Common(
        message="Artist deleted successfully"
    ).exception_handler
    def delete(self, request):
        data = request.validated_data

        updated = Artist.deactivate(data.artist_id)
        if not updated:
            raise ValueError("Artist not found")

        return {}

