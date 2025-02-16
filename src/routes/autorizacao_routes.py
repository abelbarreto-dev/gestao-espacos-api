from typing import Any

from fastapi import APIRouter

from src.controllers.autorizacao_controller import AutorizacaoController
from src.domain.dtos.autorizacao import Autorizacao


authorize_controller = AutorizacaoController()
authorize_routes = APIRouter()


@authorize_routes.post("/autorizacoes")
def create_historico(historico: Autorizacao) -> Any:
    return authorize_controller.create_autorizacao(historico)


@authorize_routes.get("/autorizacoes")
def find_all_historicos() -> Any:
    return authorize_controller.find_all_autorizacaos()


@authorize_routes.get("/autorizacoes/{id}")
def find_historico_by_id(id: int) -> Any:
    return authorize_controller.find_autorizacao_by_id(id)


@authorize_routes.put("/autorizacoes/{id}")
def update_historico(historico: dict, id: int) -> Any:
    return authorize_controller.update_autorizacao(historico, id)


@authorize_routes.delete("/autorizacoes/{id}")
def delete_historico(id: int) -> Any:
    return authorize_controller.delete_autorizacao_by_id(id)
