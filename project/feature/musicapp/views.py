from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage

from common.utilities import Utils
from project.feature.musicapp.models.model import Music
from project.feature.musicapp.serializer.request.create import CreateMusicSerializer
from project.feature.musicapp.serializer.request.update import UpdateMusicSerializer
from project.feature.musicapp.serializer.request.partial_update import PartialUpdateMusicSerializer
from project.feature.musicapp.serializer.response.music_detail import MusicDetailResponseSerializer
from project.feature.musicapp.serializer.response.music_list import MusicListResponseSerializer


def create_music(request):
    serializer = CreateMusicSerializer(data=request.data)
    validation = Utils.validate(serializer)
    if validation is not True:
        return validation

    music = Music.objects.create(**serializer.validated_data)

    return Response(
        Utils.success_response(
            message="Music created successfully",
            data=MusicDetailResponseSerializer.serialize(music)
        ),
        status=status.HTTP_201_CREATED
    )


def list_music(request):
    queryset = Music.objects.filter(is_active=True).order_by("-id")


    params = Utils.get_query_params(request)
    page_num = int(params.get("page_num", 1))
    limit = int(params.get("limit", 10))


    paginator = Paginator(queryset, limit)

    try:
        page = paginator.page(page_num)
        serialized_data = MusicListResponseSerializer.serialize(page)
    except EmptyPage:
        serialized_data = []

    # 🔹 Wrap with pagination metadata
    final_data = Utils.add_page_parameter(
        final_data=serialized_data,
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


def retrieve_music(request):
    table_code = request.GET.get("tableCode")

    if not table_code:
        return Response(
            Utils.error_response("tableCode is required"),
            status=status.HTTP_400_BAD_REQUEST
        )

    music_id = int(table_code.split("-")[-1])
    music = get_object_or_404(Music, id=music_id)

    return Response(
        Utils.success_response(
            message="Music fetched successfully",
            data=MusicDetailResponseSerializer.serialize(music)
        ),
        status=status.HTTP_200_OK
    )


def update_music(request):
    table_code = request.GET.get("tableCode")
    music_id = int(table_code.split("-")[-1])
    music = get_object_or_404(Music, id=music_id)

    serializer = (
        UpdateMusicSerializer(data=request.data)
        if request.method == "PUT"
        else PartialUpdateMusicSerializer(data=request.data, partial=True)
    )

    validation = Utils.validate(serializer)
    if validation is not True:
        return validation

    for k, v in serializer.validated_data.items():
        setattr(music, k, v)
    music.save()

    return Response(
        Utils.success_response(
            message="Music updated successfully",
            data=MusicDetailResponseSerializer.serialize(music)
        ),
        status=status.HTTP_200_OK
    )


def delete_music(request):
    table_code = request.GET.get("tableCode")
    music_id = int(table_code.split("-")[-1])
    music = get_object_or_404(Music, id=music_id)

    music.is_active = False
    music.save()

    return Response(
        Utils.success_response(message="Music deleted successfully"),
        status=status.HTTP_200_OK
    )
