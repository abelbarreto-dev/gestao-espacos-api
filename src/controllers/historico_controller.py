from typing import List, Any, Optional

from src.domain.db.historico import Historico as HistoricoDB
from src.domain.dtos.historico import Historico
from src.exceptions.http_exception import HTTPError
from src.response.response import response_builder
from src.services.historico_service import HistoricoService


class HistoricoController:
    def __init__(self):
        self.story_service = HistoricoService()

    def create_historico(self, historico: Historico) -> Any:
        try:
            data = self.story_service.create_historico(historico)

            response = response_builder(data=data.model_dump())
            return response
        except Exception as ex:
            raise HTTPError(str(ex))

    def find_all_historicos(self) -> Any:
        try:
            data = self.story_service.find_all_historicos()

            response = response_builder(data=data)
            return response
        except Exception as ex:
            raise HTTPError(str(ex))

    def find_historico_by_id(self, id: int) -> Any:
        try:
            data = self.story_service.find_historico_by_id(id)

            response = response_builder(data=data.model_dump())
            return response
        except Exception as ex:
            raise HTTPError(str(ex))

    def filter_historico_by_solicitacao_id(self, solicitacao_id: Optional[int] = None) -> Any:
        try:
            if solicitacao_id is None:
                raise Exception("Solicitacao Id is Required")

            data = self.story_service.filter_historico_by_solicitacao_id(solicitacao_id)

            response = response_builder(data=data)
            return response
        except Exception as ex:
            raise HTTPError(str(ex))

    def update_historico(self, historico: dict, id: int) -> Any:
        try:
            story_db = HistoricoDB(**historico)

            data = self.story_service.update_historico(story_db, id)

            response = response_builder(data=data.model_dump())
            return response
        except Exception as ex:
            raise HTTPError(str(ex))

    def delete_historico_by_id(self, id: int) -> Any:
        try:
            data = self.story_service.delete_historico_by_id(id)

            response = response_builder(data=data.model_dump())
            return response
        except Exception as ex:
            raise HTTPError(str(ex))
