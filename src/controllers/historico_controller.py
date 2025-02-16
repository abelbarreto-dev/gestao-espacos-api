from typing import List, Any

from src.domain.db.historico import Historico as HistoricoDB
from src.domain.dtos.historico import Historico
from src.exceptions.http_exception import HTTPError
from src.services.historico_service import HistoricoService


class HistoricoController:
    def __init__(self):
        self.story_service = HistoricoService()

    def create_historico(self, historico: Historico) -> Historico:
        try:
            return self.story_service.create_historico(historico)
        except Exception as ex:
            raise HTTPError(str(ex))

    def find_all_historicos(self) -> List:
        try:
            return self.story_service.find_all_historicos()
        except Exception as ex:
            raise HTTPError(str(ex))

    def find_historico_by_id(self, id: int) -> Any:
        try:
            return self.story_service.find_historico_by_id(id)
        except Exception as ex:
            raise HTTPError(str(ex))

    def update_historico(self, historico: dict, id: int) -> Any:
        try:
            story_db = HistoricoDB(**historico)

            return self.story_service.update_historico(story_db, id)
        except Exception as ex:
            raise HTTPError(str(ex))

    def delete_historico_by_id(self, id: int) -> Any:
        try:
            return self.story_service.delete_historico_by_id(id)
        except Exception as ex:
            raise HTTPError(str(ex))
