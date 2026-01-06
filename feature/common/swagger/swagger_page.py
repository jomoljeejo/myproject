

from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, OpenApiResponse
from rest_framework import status
from rest_framework import serializers


# SIMPLE generic response serializers (you don’t have any yet)
class SuccessResponseSerializer(serializers.Serializer):
    message = serializers.CharField()
    data = serializers.JSONField(required=False)


class FailureResponseSerializer(serializers.Serializer):
    message = serializers.CharField()
    errors = serializers.JSONField(required=False)


class SwaggerPage:
    """
    Common Swagger helper (like your reference project)
    """

    @staticmethod
    def list_parameters():
        return [
            OpenApiParameter(
                name="page_num",
                description="Page number",
                required=False,
                type=OpenApiTypes.INT,
                location=OpenApiParameter.QUERY,
            ),
            OpenApiParameter(
                name="limit",
                description="Items per page",
                required=False,
                type=OpenApiTypes.INT,
                location=OpenApiParameter.QUERY,
            ),
        ]

    @staticmethod
    def response(response=None):
        responses = {
            status.HTTP_400_BAD_REQUEST: OpenApiResponse(
                description="Bad Request",
                response=FailureResponseSerializer,
            ),
            status.HTTP_500_INTERNAL_SERVER_ERROR: OpenApiResponse(
                description="Server Error",
                response=FailureResponseSerializer,
            ),
        }

        if response:
            responses[status.HTTP_200_OK] = OpenApiResponse(
                description="Success",
                response=response,
            )
        else:
            responses[status.HTTP_200_OK] = OpenApiResponse(
                description="Success",
                response=SuccessResponseSerializer,
            )

        return responses
