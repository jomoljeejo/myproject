from typing import Any, Dict, List, Optional, Union
from rest_framework import status
from rest_framework.response import Response
from urllib.parse import unquote


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


    @staticmethod
    def get_query_params(request) -> Dict[str, str]:
        """
        Extract query parameters safely from request
        """
        try:
            url = request.get_full_path()
        except Exception:
            url = request.path

        params = {}

        if "?" in url:
            query_string = unquote(url.split("?", 1)[1])
            for param in query_string.split("&"):
                if "=" in param:
                    key, value = param.split("=", 1)
                    params[key] = value
                else:
                    params[param] = ""

        return params

    @staticmethod
    def add_page_parameter(
        final_data: Union[List, Dict],
        page_num: int,
        total_page: int,
        total_count: int,
        present_url: str,
        next_page_required: bool = False
    ) -> Dict[str, Any]:
        """
        Wrap paginated data with metadata
        """
        response = {
            "data": final_data,
            "presentPage": page_num,
            "totalPage": total_page,
            "totalCount": total_count
        }

        if next_page_required and page_num < total_page:
            if "page_num=" in present_url:
                response["nextPageUrl"] = present_url.replace(
                    f"page_num={page_num}",
                    f"page_num={page_num + 1}"
                )
            else:
                separator = "&" if "?" in present_url else "?"
                response["nextPageUrl"] = (
                    f"{present_url}{separator}page_num={page_num + 1}"
                )

        return response
