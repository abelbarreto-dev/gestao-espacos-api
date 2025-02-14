from typing import Any

from src.domain.db.espaco_publico import EspacoPublico as EspacoDB
from src.domain.dtos.espaco_publico import EspacoPublico
from src.exceptions.http_exception import HTTPError
from src.services.espaco_publico_service import EspacoPublicoService


class EspacoPublicoController:
    def __init__(self):
        self.esp_pub_service = EspacoPublicoService()

    def create_espaco_publico(self, espaco_publico: EspacoPublico) -> Any:
        try:
            return self.esp_pub_service.create_espaco_publico(espaco_publico)
        except Exception as ex:
            raise HTTPError(str(ex))

    def find_all_espaco_publicos(self) -> Any:
        try:
            return self.esp_pub_service.find_all_espaco_publicos()
        except Exception as ex:
            raise HTTPError(str(ex))

    def find_espaco_publico_by_id(self, id: int) -> Any:
        try:
            return self.esp_pub_service.find_espaco_publico_by_id(id)
        except Exception as ex:
            raise HTTPError(str(ex))

    def update_espaco_publico(self, espaco_publico: dict, id: int) -> Any:
        try:
            espaco_db = EspacoDB(**espaco_publico)
            return self.esp_pub_service.update_espaco_publico(espaco_db, id)
        except Exception as ex:
            raise HTTPError(str(ex))

    def delete_espaco_publico_by_id(self, id: int) -> Any:
        try:
            return self.esp_pub_service.delete_espaco_publico_by_id(id)
        except Exception as ex:
            raise HTTPError(str(ex))
