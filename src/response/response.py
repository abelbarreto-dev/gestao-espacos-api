from fastapi import status
from fastapi.responses import JSONResponse
from typing import Any, Dict, Optional


def response_builder(
    status_code: int = status.HTTP_200_OK,
    message: str = "Operation Ok",
    data: Optional[Any] = None,
    meta: Optional[Dict[str, Any]] = None,
    status_type: str = "success"
) -> JSONResponse:
    response_data = {
        "status": status_type,
        "message": message,
        "data": data if data is not None else {},
        "meta": meta if meta is not None else {}
    }

    return JSONResponse(content=response_data, status_code=status_code)
