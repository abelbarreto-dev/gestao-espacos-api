from typing import Any

from fastapi import APIRouter

from src.controllers.solicitante_controller import SolicitanteController
from src.domain.dtos.solicitante import Solicitante


solicit_controller = SolicitanteController()
solicit_router = APIRouter()


@solicit_router.post("/solicitantes")
def create_solicitante(solicitante: Solicitante) -> Any:
    return solicit_controller.create_solicitante(solicitante)


@solicit_router.get("/solicitantes")
def find_all_solicitantes() -> Any:
    return solicit_controller.find_all_solicitantes()


@solicit_router.get("/solicitantes/{id}")
def find_solicitante_by_id(id: int) -> Any:
    return solicit_controller.find_solicitante_by_id(id)


@solicit_router.put("/solicitantes/{id}")
def update_solicitante_by_id(solicitante: dict, id: int) -> Any:
    return solicit_controller.update_solicitante_by_id(solicitante, id)


@solicit_router.delete("/solicitantes/{id}")
def delete_solicitante_by_id(id: int) -> Any:
    return solicit_controller.delete_solicitante_by_id(id)
