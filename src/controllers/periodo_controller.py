from typing import Any

from src.domain.db.periodo import Periodo as PeriodoDB
from src.domain.dtos.periodo import Periodo
from src.exceptions.http_exception import HTTPError
from src.response.response import response_builder
from src.services.periodo_service import PeriodoService


class PeriodoController:
    def __init__(self):
        self.periodo_service = PeriodoService()

    def create_periodo(self, periodo: Periodo) -> Any:
        try:
            data = self.periodo_service.create_periodo(periodo)

            response = response_builder(data=data.model_dump())
            return response
        except Exception as ex:
            raise HTTPError(str(ex))

    def find_all_periodos(self) -> Any:
        try:
            data = self.periodo_service.find_all_periodos()

            response = response_builder(data=data)
            return response
        except Exception as ex:
            raise HTTPError(str(ex))

    def find_periodo_by_id(self, id: int) -> Any:
        try:
            data = self.periodo_service.find_periodo_by_id(id)

            response = response_builder(data=data.model_dump())
            return response
        except Exception as ex:
            raise HTTPError(str(ex))

    def update_periodo(self, periodo: dict, id: int) -> Any:
        try:
            new_periodo = PeriodoDB(**periodo)

            data = self.periodo_service.update_periodo(new_periodo, id)

            response = response_builder(data=data.model_dump())
            return response
        except Exception as ex:
            raise HTTPError(str(ex))

    def delete_periodo_by_id(self, id: int) -> Any:
        try:
            data = self.periodo_service.delete_periodo_by_id(id)

            response = response_builder(data=data.model_dump())
            return response
        except Exception as ex:
            raise HTTPError(str(ex))
