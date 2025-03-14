from typing import Any, Optional

from src.domain.db.solicitacao import Solicitacao as SolicitacaoDB
from src.domain.dtos.solicitacao import Solicitacao
from src.exceptions.http_exception import HTTPError
from src.response.response import response_builder
from src.services.solicitacao_service import SolicitacaoService


class SolicitacaoController:
    def __init__(self):
        self.solicit_service = SolicitacaoService()

    def create_solicitacao(self, solicitaco: Solicitacao) -> Any:
        try:
            data = self.solicit_service.create_solicitacao(solicitaco)

            response = response_builder(data=data.model_dump())
            return response
        except Exception as ex:
            raise HTTPError(str(ex))

    def find_all_solicitacaos(self) -> Any:
        try:
            data = self.solicit_service.find_all_solicitacaos()

            response = response_builder(data=data)
            return response
        except Exception as ex:
            raise HTTPError(str(ex))

    def find_solicitacao_by_id(self, id: int) -> Any:
        try:
            data = self.solicit_service.find_solicitacao_by_id(id)

            response = response_builder(data=data.model_dump())
            return response
        except Exception as ex:
            raise HTTPError(str(ex))

    def filter_solicitacao_by_status_or_solicitante_id(self, status: Optional[str] = None, solicitante_id: Optional[int] = None) -> Any:
        try:
            if status is None and solicitante_id is None:
                raise Exception("Solicitante Id or Status is Required")

            data = (
                self.solicit_service.filter_solicitacao_by_status(status) if status
                else self.solicit_service.filter_solicitacao_by_solicitante_id(solicitante_id)
                if solicitante_id else None
            )

            response = response_builder(data=data)
            return response
        except Exception as ex:
            raise HTTPError(str(ex))

    def filter_solicitacao_by_status(self, status: str) -> Any:
        try:
            data = self.solicit_service.filter_solicitacao_by_status(status)

            response = response_builder(data=data)
            return response
        except Exception as ex:
            raise HTTPError(str(ex))

    def update_solicitacao(self, solicitacao: dict, id: int) -> Any:
        try:
            new_solicitacao = SolicitacaoDB(**solicitacao)
            data = self.solicit_service.update_solicitacao(new_solicitacao, id)

            response = response_builder(data=data.model_dump())
            return response
        except Exception as ex:
            raise HTTPError(str(ex))

    def delete_solicitacao_by_id(self, id: int) -> Any:
        try:
            data = self.solicit_service.delete_solicitacao_by_id(id)

            response = response_builder(data=data.model_dump())
            return response
        except Exception as ex:
            raise HTTPError(str(ex))
