from functools import wraps
from django.db.models.query import QuerySet
from rest_framework.response import Response
from rest_framework import status

from feature.common.utilities import Utils


class Common:
    def __init__(self, *, response_handler=None, message=None, status_code=None):
        self.response_handler = response_handler
        self.message = message
        self.status_code = status_code or status.HTTP_200_OK

    def exception_handler(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)


                if isinstance(result, Response):
                    return result


                many = isinstance(result, (list, tuple, QuerySet))

                if self.response_handler:
                    if many:
                        result = [
                            self.response_handler.serialize(obj)
                            for obj in result
                        ]
                    else:
                        result = self.response_handler.serialize(result)

                return Response(
                    Utils.success_response(
                        message=self.message,
                        data=result
                    ),
                    status=self.status_code
                )

            except ValueError as e:
                return Response(
                    Utils.error_response("Validation error", str(e)),
                    status=status.HTTP_400_BAD_REQUEST
                )

            except Exception as e:
                return Response(
                    Utils.error_response("Something went wrong", str(e)),
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

        return wrapper
