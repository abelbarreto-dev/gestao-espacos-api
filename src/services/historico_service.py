from typing import List, Any

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
        return self.story_repo.create_historico(historico_db)

    def find_all_historicos(self) -> List:
        return self.story_repo.find_all_historicos()

    def find_historico_by_id(self, id: int) -> Any:
        return self.story_repo.find_historico_by_id(id)

    def update_historico(self, historico: HistoricoDB) -> Any:
        HistoricoUtil.check_all(historico)

        return self.story_repo.update_historico(historico)

    def delete_historico_by_id(self, id: int) -> Any:
        return self.story_repo.delete_historico_by_id(id)
