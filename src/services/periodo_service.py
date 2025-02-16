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
        return self.periodo_repo.create_periodo(periodo_db)

    def find_all_periodos(self) -> List:
        return self.periodo_repo.find_all_periodos()

    def find_periodo_by_id(self, id: int) -> Any:
        return self.periodo_repo.find_periodo_by_id(id)

    def update_periodo(self, periodo: PeriodoDB, id: int) -> Any:
        PeriodoUtil.check_all(periodo)

        return self.periodo_repo.update_periodo(periodo, id)

    def delete_periodo_by_id(self, id: int) -> Any:
        return self.periodo_repo.delete_periodo_by_id(id)
