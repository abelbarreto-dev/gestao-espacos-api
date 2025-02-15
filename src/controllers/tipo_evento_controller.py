from typing import Any

from src.domain.db.tipo_evento import TipoEvento as TipoEventoDB
from src.domain.dtos.tipo_evento import TipoEvento
from src.exceptions.http_exception import HTTPError
from src.services.tipo_evento_service import TipoEventoService


class TipoEventoController:
    def __init__(self):
        self.tipo_evento_service = TipoEventoService()

    def create_tipo_evento(self, tipo_evento: TipoEvento) -> Any:
        try:
            return self.tipo_evento_service.create_tipo_evento(tipo_evento)
        except Exception as ex:
            raise HTTPError(str(ex))

    def find_all_tipo_eventos(self) -> Any:
        try:
            return self.tipo_evento_service.find_all_tipo_eventos()
        except Exception as ex:
            raise HTTPError(str(ex))

    def find_tipo_evento_by_id(self, id: int) -> Any:
        try:
            return self.tipo_evento_service.find_tipo_evento_by_id(id)
        except Exception as ex:
            raise HTTPError(str(ex))

    def update_tipo_evento(self, tipo_evento: dict, id: int) -> Any:
        try:
            evento_tipo = TipoEventoDB(**tipo_evento)
            return self.tipo_evento_service.update_tipo_evento(evento_tipo, id)
        except Exception as ex:
            raise HTTPError(str(ex))

    def delete_tipo_evento_by_id(self, id: int) -> Any:
        try:
            return self.tipo_evento_service.delete_tipo_evento_by_id(id)
        except Exception as ex:
            raise HTTPError(str(ex))
