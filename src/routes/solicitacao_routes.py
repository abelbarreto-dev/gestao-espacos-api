from typing import Any, Optional

from fastapi import APIRouter

from src.controllers.solicitacao_controller import SolicitacaoController
from src.domain.dtos.solicitacao import Solicitacao


solicit_controller = SolicitacaoController()
solicitacao_routes = APIRouter()


@solicitacao_routes.post("/solicitacoes")
def create_solicitacao(solicitaco: Solicitacao) -> Any:
    return solicit_controller.create_solicitacao(solicitaco)


@solicitacao_routes.get("/solicitacoes")
def find_all_solicitacaos() -> Any:
    return solicit_controller.find_all_solicitacaos()


@solicitacao_routes.get("/solicitacoes/{id}")
def find_solicitacao_by_id(id: int) -> Any:
    return solicit_controller.find_solicitacao_by_id(id)


@solicitacao_routes.get("/solicitacoes/filter")
def filter_solicitacao_by_status(
        status: Optional[str] = None,
        solicitante_id: Optional[int] = None
) -> Any:
    return solicit_controller.filter_solicitacao_by_status_or_solicitante_id(
        status,
        solicitante_id
    )


@solicitacao_routes.put("/solicitacoes/{id}")
def update_solicitacao(solicitacao: dict, id: int) -> Any:
    return solicit_controller.update_solicitacao(solicitacao, id)


@solicitacao_routes.delete("/solicitacoes/{id}")
def delete_solicitacao_by_id(id: int) -> Any:
    return solicit_controller.delete_solicitacao_by_id(id)
