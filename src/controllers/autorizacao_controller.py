from typing import Any

from src.domain.db.autorizacao import Autorizacao as AutorizacaoDB
from src.domain.dtos.autorizacao import Autorizacao
from src.exceptions.http_exception import HTTPError
from src.response.response import response_builder
from src.services.autorizacao_service import AutorizacaoService


class AutorizacaoController:
    def __init__(self):
        self.auth_service = AutorizacaoService()

    def create_autorizacao(self, autorizacao: Autorizacao) -> Any:
        try:
            data = self.auth_service.create_autorizacao(autorizacao)

            response = response_builder(data=data.model_dump())
            return response
        except Exception as ex:
            raise HTTPError(str(ex))

    def find_all_autorizacaos(self) -> Any:
        try:
            data = self.auth_service.find_all_autorizacaos()

            response = response_builder(data=data)
            return response
        except Exception as ex:
            raise HTTPError(str(ex))

    def find_autorizacao_by_id(self, id: int) -> Any:
        try:
            data = self.auth_service.find_autorizacao_by_id(id)

            response = response_builder(data=data.model_dump())
            return response
        except Exception as ex:
            raise HTTPError(str(ex))

    def update_autorizacao(self, autorizacao: dict, id: int) -> Any:
        try:
            author_db = AutorizacaoDB(**autorizacao)

            data = self.auth_service.update_autorizacao(author_db, id)

            response = response_builder(data=data.model_dump())
            return response
        except Exception as ex:
            raise HTTPError(str(ex))

    def delete_autorizacao_by_id(self, id: int) -> Any:
        try:
            data = self.auth_service.delete_autorizacao_by_id(id)

            response = response_builder(data=data.model_dump())
            return response
        except Exception as ex:
            raise HTTPError(str(ex))
