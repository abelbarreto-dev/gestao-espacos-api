from typing import Any

from src.domain.db.solicitacao import Solicitacao as SolicitacaoDB
from src.domain.dtos.solicitacao import Solicitacao
from src.exceptions.http_exception import HTTPError
from src.services.solicitacao_service import SolicitacaoService


class SolicitacaoController:
    def __init__(self):
        self.solicit_service = SolicitacaoService()

    def create_solicitacao(self, solicitaco: Solicitacao) -> Solicitacao:
        try:
            return self.solicit_service.create_solicitacao(solicitaco)
        except Exception as ex:
            raise HTTPError(str(ex))

    def find_all_solicitacaos(self) -> Any:
        try:
            return self.solicit_service.find_all_solicitacaos()
        except Exception as ex:
            raise HTTPError(str(ex))

    def find_solicitacao_by_id(self, id: int) -> Any:
        try:
            return self.solicit_service.find_solicitacao_by_id(id)
        except Exception as ex:
            raise HTTPError(str(ex))

    def update_solicitacao(self, solicitacao: dict, id: int) -> Any:
        try:
            new_solicitacao = SolicitacaoDB(**solicitacao)
            return self.solicit_service.update_solicitacao(new_solicitacao, id)
        except Exception as ex:
            raise HTTPError(str(ex))

    def delete_solicitacao_by_id(self, id: int) -> Any:
        try:
            return self.solicit_service
        except Exception as ex:
            raise HTTPError(str(ex))
