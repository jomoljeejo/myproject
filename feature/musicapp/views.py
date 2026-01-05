from rest_framework.response import Response
from rest_framework import status
from django.core.paginator import Paginator, EmptyPage

from feature.common.utilities import Utils
from feature.common.common import Common
from feature.musicapp.models.model import Music
from feature.musicapp.serializer.response.music_detail import (
    MusicDetailResponseSerializer
)
from feature.musicapp.serializer.response.music_list import (
    MusicListResponseSerializer
)


class MusicView:

    @Common(
        response_handler=MusicDetailResponseSerializer,
        message="Music created successfully",
        status_code=status.HTTP_201_CREATED
    ).exception_handler
    def create(self, request):
        try:
            return Music.create(**request.validated_data)
        except ValueError as e:
            raise ValueError(str(e))


    def list_music(self, request):
        data = request.validated_data
        page_num = data["page_num"]
        limit = data["limit"]

        queryset = Music.get_all()
        paginator = Paginator(queryset, limit)

        try:
            page = paginator.page(page_num)
            serialized = [
                MusicListResponseSerializer.serialize(obj)
                for obj in page
            ]
        except EmptyPage:
            serialized = []

        final_data = Utils.add_page_parameter(
            final_data=serialized,
            page_num=page_num,
            total_page=paginator.num_pages,
            total_count=paginator.count,
            present_url=request.get_full_path(),
            next_page_required=True
        )

        return Response(
            Utils.success_response(
                message="Music list fetched successfully",
                data=final_data
            ),
            status=status.HTTP_200_OK
        )


    @Common(
        response_handler=MusicDetailResponseSerializer,
        message="Music fetched successfully"
    ).exception_handler
    def retrieve(self, request):
        music_id = self._get_music_id(request)
        if isinstance(music_id, Response):
            return music_id

        music = Music.get_one(music_id)
        if not music:
            raise ValueError("Music not found")

        return music

    @Common(
        response_handler=MusicDetailResponseSerializer,
        message="Music updated successfully"
    ).exception_handler
    def update(self, request):
        music_id = self._get_music_id(request)
        if isinstance(music_id, Response):
            return music_id

        data = request.validated_data.copy()
        data.pop("tableCode", None)

        try:
            music = Music.update(music_id, **data)
        except ValueError as e:
            raise ValueError(str(e))

        if not music:
            raise ValueError("Music not found")

        return music

    @Common(
        message="Music deleted successfully"
    ).exception_handler
    def delete(self, request):
        music_id = self._get_music_id(request)
        if isinstance(music_id, Response):
            return music_id

        success = Music.delete_one(music_id)
        if not success:
            raise ValueError("Music not found")

        return {}

    def _get_music_id(self, request):
        table_code = request.validated_data.get("tableCode")

        try:
            return int(table_code.split("-")[-1])
        except Exception:
            return Response(
                Utils.error_response(
                    "Invalid tableCode format",
                    "Expected format: MUSIC-<id>"
                ),
                status=status.HTTP_400_BAD_REQUEST
            )
