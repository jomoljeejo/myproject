from typing import Any, Dict, List, Optional, Union
from rest_framework import status
from rest_framework.response import Response


class Utils:
    """
    Common response utility for the entire project
    """

    @staticmethod
    def success_response(
        message: str,
        data: Optional[Union[Dict, List]] = None
    ) -> Dict[str, Any]:
        response = {
            "status": True,
            "message": message
        }

        if data is not None:
            response["data"] = data

        return response

    @staticmethod
    def error_response(
        message: str,
        error: Optional[Union[str, List[str]]] = None
    ) -> Dict[str, Any]:
        response = {
            "status": False,
            "message": message
        }

        if error is not None:
            response["error"] = error

        return response

    @staticmethod
    def validate(serializer):
        if not serializer.is_valid():
            return Response(
                Utils.error_response(
                    message="Validation Error",
                    error=Utils.flatten_errors(serializer.errors)
                ),
                status=status.HTTP_400_BAD_REQUEST
            )
        return True

    @staticmethod
    def flatten_errors(errors, parent_key="") -> List[str]:
        flat = []

        if isinstance(errors, dict):
            for key, value in errors.items():
                field = key.replace("_", " ").title()
                full = f"{parent_key}.{field}" if parent_key else field
                flat.extend(Utils.flatten_errors(value, full))
        elif isinstance(errors, list):
            for item in errors:
                flat.extend(Utils.flatten_errors(item, parent_key))
        else:
            flat.append(f"{parent_key}: {errors}")

        return flat
