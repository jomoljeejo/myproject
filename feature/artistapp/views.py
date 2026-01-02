from rest_framework.response import Response
from rest_framework import status
from django.core.paginator import Paginator, EmptyPage

from feature.artistapp.model.model import Artist
from feature.artistapp.serializer.response.artist_detail import (
    ArtistDetailResponseSerializer
)
from feature.common.utilities import Utils


class ArtistView:

    def create(self, request):
        artist = Artist.objects.create(
            name=request.validated_data["name"],
            country=request.validated_data.get("country")
        )

        return Response(
            Utils.success_response(
                message="Artist created successfully",
                data=ArtistDetailResponseSerializer.serialize(artist)
            ),
            status=status.HTTP_201_CREATED
        )

    def list_artist(self, request):
        data = request.validated_data
        paginator = Paginator(Artist.get_all(), data["limit"])

        try:
            page = paginator.page(data["page_num"])
            serialized = [
                ArtistDetailResponseSerializer.serialize(obj)
                for obj in page
            ]
        except EmptyPage:
            serialized = []

        final_data = Utils.add_page_parameter(
            final_data=serialized,
            page_num=data["page_num"],
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
