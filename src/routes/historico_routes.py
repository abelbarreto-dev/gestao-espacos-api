from typing import Any

from fastapi import APIRouter

from src.controllers.historico_controller import HistoricoController
from src.domain.dtos.historico import Historico

story_controller = HistoricoController()
story_routes = APIRouter()


@story_routes.post("/historico-solicitacoes")
def create_historico(historico: Historico) -> Any:
    return story_controller.create_historico(historico)


@story_routes.get("/historico-solicitacoes")
def find_all_historicos() -> Any:
    return story_controller.find_all_historicos()


@story_routes.get("/historico-solicitacoes/{id}")
def find_historico_by_id(id: int) -> Any:
    return story_controller.find_historico_by_id(id)


@story_routes.put("/historico-solicitacoes/{id}")
def update_historico(historico: dict, id: int) -> Any:
    return story_controller.update_historico(historico, id)


@story_routes.delete("/historico-solicitacoes/{id}")
def delete_historico_by_id(id: int) -> Any:
    return story_controller.delete_historico_by_id(id)
