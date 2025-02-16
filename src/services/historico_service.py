from typing import Any

from src.domain.db.historico import Historico as HistoricoDB
from src.domain.dtos.historico import Historico
from src.repository.historico_repository import HistoricoRepository
from src.utilities.historico_util import HistoricoUtil


class HistoricoService:
    def __init__(self):
        self.story_repo = HistoricoRepository()

    def create_historico(self, historico: Historico) -> Historico:
        HistoricoUtil.check_all(historico)

        historico_db = HistoricoUtil.to_historico_db(historico)
        historico_db = self.story_repo.create_historico(historico_db)

        response = HistoricoUtil.from_db_to_base_model(historico_db)
        return response

    def find_all_historicos(self) -> Any:
        historico = self.story_repo.find_all_historicos()

        response = HistoricoUtil.from_db_list_to_base_model(historico)
        return response

    def find_historico_by_id(self, id: int) -> Any:
        historico = self.story_repo.find_historico_by_id(id)

        response = HistoricoUtil.from_db_list_to_base_model(historico)
        return response

    def filter_historico_by_solicitacao_id(self, solicitacao_id: int) -> Any:
        historico = self.story_repo.filter_historico_by_solicitacao_id(solicitacao_id)

        response = HistoricoUtil.from_db_list_to_base_model(historico)
        return response

    def update_historico(self, historico: HistoricoDB, id: int) -> Any:
        HistoricoUtil.check_all(historico)

        historico_db = self.story_repo.update_historico(historico, id)

        response = HistoricoUtil.from_db_to_base_model(historico_db)
        return response

    def delete_historico_by_id(self, id: int) -> Any:
        return self.story_repo.delete_historico_by_id(id)
