from typing import Any

from src.domain.db.periodo import Periodo as PeriodoDB
from src.domain.dtos.periodo import Periodo
from src.exceptions.http_exception import HTTPError
from src.services.periodo_service import PeriodoService


class PeriodoController:
    def __init__(self):
        self.periodo_service = PeriodoService()

    def create_periodo(self, periodo: Periodo) -> Periodo:
        try:
            return self.periodo_service.create_periodo(periodo)
        except Exception as ex:
            raise HTTPError(str(ex))

    def find_all_periodos(self) -> Any:
        try:
            return self.periodo_service.find_all_periodos()
        except Exception as ex:
            raise HTTPError(str(ex))

    def find_periodo_by_id(self, id: int) -> Any:
        try:
            return self.periodo_service.find_periodo_by_id(id)
        except Exception as ex:
            raise HTTPError(str(ex))

    def update_periodo(self, periodo: dict, id: int) -> Any:
        try:
            new_periodo = PeriodoDB(**periodo)

            return self.periodo_service.update_periodo(new_periodo, id)
        except Exception as ex:
            raise HTTPError(str(ex))

    def delete_periodo_by_id(self, id: int) -> Any:
        try:
            return self.periodo_service.delete_periodo_by_id(id)
        except Exception as ex:
            raise HTTPError(str(ex))
