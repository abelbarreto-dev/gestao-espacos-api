from typing import List, Any

from src.domain.db.periodo import Periodo as PeriodoDB
from src.domain.dtos.periodo import Periodo
from src.repository.periodo_repository import PeriodoRepository
from src.utilities.periodo_util import PeriodoUtil


class PeriodoService:
    def __init__(self):
        self.periodo_repo = PeriodoRepository()

    def create_periodo(self, periodo: Periodo) -> Periodo:
        PeriodoUtil.check_all(periodo)

        periodo_db = PeriodoUtil.to_periodo_db(periodo)
        periodo_db = self.periodo_repo.create_periodo(periodo_db)

        response = PeriodoUtil.from_db_to_base_model(periodo_db)
        return response

    def find_all_periodos(self) -> List:
        all_periodos = self.periodo_repo.find_all_periodos()

        response = PeriodoUtil.from_db_list_to_base_model(all_periodos)
        return response

    def find_periodo_by_id(self, id: int) -> Any:
        seacon = self.periodo_repo.find_periodo_by_id(id)

        response = PeriodoUtil.from_db_to_base_model(seacon)
        return response

    def update_periodo(self, periodo: PeriodoDB, id: int) -> Any:
        PeriodoUtil.check_all(periodo)

        seacon = self.periodo_repo.update_periodo(periodo, id)

        response = PeriodoUtil.from_db_to_base_model(seacon)
        return response

    def delete_periodo_by_id(self, id: int) -> Any:
        return self.periodo_repo.delete_periodo_by_id(id)
