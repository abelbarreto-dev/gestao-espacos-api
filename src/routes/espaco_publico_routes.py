from typing import Any

from fastapi import APIRouter

from src.controllers.espaco_publico_controller import EspacoPublicoController
from src.domain.dtos.espaco_publico import EspacoPublico


esp_pub_controller = EspacoPublicoController()
espaco_publico_routes = APIRouter()


@espaco_publico_routes.post("/espacos-publicos")
def create_espaco_publico(espaco_publico: EspacoPublico) -> Any:
    return esp_pub_controller.create_espaco_publico(espaco_publico)


@espaco_publico_routes.get("/espacos-publicos")
def find_all_espaco_publicos() -> Any:
    return esp_pub_controller.find_all_espaco_publicos()


@espaco_publico_routes.get("/espacos-publicos/{id}")
def find_espaco_publico_by_id(id: int) -> Any:
    return esp_pub_controller.find_espaco_publico_by_id(id)


@espaco_publico_routes.put("/espacos-publicos/{id}")
def update_espaco_publico(espaco_publico: dict, id: int) -> Any:
    return esp_pub_controller.update_espaco_publico(espaco_publico, id)


@espaco_publico_routes.delete("/espacos-publicos/{id}")
def delete_espaco_publico_by_id(id: int) -> Any:
    return esp_pub_controller.delete_espaco_publico_by_id(id)
