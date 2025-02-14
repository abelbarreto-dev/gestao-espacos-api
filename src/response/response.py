from fastapi.openapi.models import Response


def response_build(content: any) -> Response:
    return Response(
        description="Status OK",
        content=content,
    )
