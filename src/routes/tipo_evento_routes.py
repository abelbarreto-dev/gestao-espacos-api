from typing import Any

from fastapi import APIRouter

from src.controllers.tipo_evento_controller import TipoEventoController
from src.domain.dtos.tipo_evento import TipoEvento

tipo_evento_control = TipoEventoController()
tipo_evento_router = APIRouter()


@tipo_evento_router.post("/tipo-evento")
def create_tipo_evento(tipo_evento: TipoEvento) -> Any:
    return tipo_evento_control.create_tipo_evento(tipo_evento)


@tipo_evento_router.get("/tipo-evento")
def find_all_tipo_eventos() -> Any:
    return tipo_evento_control.find_all_tipo_eventos()


@tipo_evento_router.get("/tipo-evento/{id}")
def find_tipo_evento_by_id(id: int) -> Any:
    return tipo_evento_control.find_tipo_evento_by_id(id)


@tipo_evento_router.put("/tipo-evento/{id}")
def update_tipo_evento(tipo_evento: dict, id: int) -> Any:
    return tipo_evento_control.update_tipo_evento(tipo_evento, id)


@tipo_evento_router.delete("/tipo-evento/{id}")
def delete_tipo_evento_by_id(id: int) -> Any:
    return tipo_evento_control.delete_tipo_evento_by_id(id)
