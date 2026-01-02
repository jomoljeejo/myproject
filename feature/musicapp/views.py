from rest_framework.response import Response
from rest_framework import status
from django.core.paginator import Paginator, EmptyPage

from feature.common.utilities import Utils
from feature.musicapp.models.model import Music
from feature.musicapp.serializer.response.music_detail import (
    MusicDetailResponseSerializer
)
from feature.musicapp.serializer.response.music_list import (
    MusicListResponseSerializer
)


class MusicView:

    def create(self, request):
        try:
            music = Music.create(**request.validated_data)
        except ValueError as e:
            return Response(
                Utils.error_response("Invalid data", str(e)),
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response(
            Utils.success_response(
                message="Music created successfully",
                data=MusicDetailResponseSerializer.serialize(music)
            ),
            status=status.HTTP_201_CREATED
        )

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

    def retrieve(self, request):
        music_id = self._get_music_id(request)
        if isinstance(music_id, Response):
            return music_id

        music = Music.get_one(music_id)
        if not music:
            return Response(
                Utils.error_response("Music not found"),
                status=status.HTTP_200_OK
            )

        return Response(
            Utils.success_response(
                message="Music fetched successfully",
                data=MusicDetailResponseSerializer.serialize(music)
            ),
            status=status.HTTP_200_OK
        )

    def update(self, request):
        music_id = self._get_music_id(request)
        if isinstance(music_id, Response):
            return music_id

        data = request.validated_data.copy()
        data.pop("tableCode", None)

        try:
            music = Music.update(music_id, **data)
        except ValueError as e:
            return Response(
                Utils.error_response("Invalid data", str(e)),
                status=status.HTTP_400_BAD_REQUEST
            )

        if not music:
            return Response(
                Utils.error_response("Music not found"),
                status=status.HTTP_200_OK
            )

        return Response(
            Utils.success_response(
                message="Music updated successfully",
                data=MusicDetailResponseSerializer.serialize(music)
            ),
            status=status.HTTP_200_OK
        )

    def delete(self, request):
        music_id = self._get_music_id(request)
        if isinstance(music_id, Response):
            return music_id

        success = Music.delete_one(music_id)
        if not success:
            return Response(
                Utils.error_response("Music not found"),
                status=status.HTTP_200_OK
            )

        return Response(
            Utils.success_response(
                message="Music deleted successfully"
            ),
            status=status.HTTP_200_OK
        )

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
