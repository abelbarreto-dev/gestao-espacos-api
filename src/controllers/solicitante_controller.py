from typing import Any

from src.domain.db.solicitante import Solicitante as SolicitanteDB
from src.domain.dtos.solicitante import Solicitante
from src.exceptions.http_exception import HTTPError
from src.response.response import response_builder
from src.services.solicitante_service import SolicitanteService


class SolicitanteController:
    def __init__(self):
        self.solicit_service = SolicitanteService()

    def create_solicitante(self, solicitante: Solicitante) -> Any:
        try:
            data = self.solicit_service.create_solicitante(solicitante)

            response = response_builder(data=data.model_dump())
            return response
        except Exception as ex:
            raise HTTPError(str(ex))

    def find_all_solicitantes(self) -> Any:
        try:
            data = self.solicit_service.find_all_solicitantes()

            response = response_builder(data=data)
            return response
        except Exception as ex:
            raise HTTPError(str(ex))

    def find_solicitante_by_id(self, id: int) -> Any:
        try:
            data = self.solicit_service.find_solicitante_by_id(id)

            response = response_builder(data=data.model_dump())
            return response
        except Exception as ex:
            raise HTTPError(str(ex))

    def update_solicitante_by_id(self, solicitante: dict, id: int) -> Any:
        try:
            solicit = SolicitanteDB(**solicitante)
            data = self.solicit_service.update_solicitante_by_id(solicit, id)

            response = response_builder(data=data.model_dump())
            return response
        except Exception as ex:
            raise HTTPError(str(ex))

    def delete_solicitante_by_id(self, id: int) -> Any:
        try:
            data = self.solicit_service.delete_solicitante_by_id(id)

            response = response_builder(data=data.model_dump())
            return response
        except Exception as ex:
            raise HTTPError(str(ex))
