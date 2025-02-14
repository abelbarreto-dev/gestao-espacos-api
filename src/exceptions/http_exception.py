from fastapi import HTTPException


class HTTPError(HTTPException):
    def __init__(self, message: str, status_code: int = 400) -> None:
        super().__init__(status_code, message)
