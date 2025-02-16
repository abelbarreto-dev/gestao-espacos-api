from typing import Any

from src.domain.db.tipo_evento import TipoEvento as TipoEventoDB
from src.domain.dtos.tipo_evento import TipoEvento
from src.repository.tipo_evento_repository import TipoEventoRepository
from src.utilities.tipo_evento_util import TipoEventoUtil


class TipoEventoService:
    def __init__(self):
        self.tipo_evento_repo = TipoEventoRepository()

    def create_tipo_evento(self, tipo_evento: TipoEvento) -> Any:
        TipoEventoUtil.check_all(tipo_evento)

        new_tipo_evento = TipoEventoUtil.to_tipo_evento_db(tipo_evento)
        new_tipo_evento = self.tipo_evento_repo.create_tipo_evento(new_tipo_evento)

        response = TipoEventoUtil.from_db_to_base_model(new_tipo_evento)
        return response

    def find_all_tipo_eventos(self) -> Any:
        all_eventos = self.tipo_evento_repo.find_all_tipo_eventos()

        response = TipoEventoUtil.from_db_list_to_base_model(all_eventos)
        return response

    def find_tipo_evento_by_id(self, id: int) -> Any:
        tipo_evento = self.tipo_evento_repo.find_tipo_evento_by_id(id)

        response = TipoEventoUtil.from_db_to_base_model(tipo_evento)
        return response

    def update_tipo_evento(self, tipo_evento: TipoEventoDB, id: int) -> Any:
        TipoEventoUtil.check_all(tipo_evento)

        tipo_evento = self.tipo_evento_repo.update_tipo_evento(tipo_evento, id)

        response = TipoEventoUtil.from_db_to_base_model(tipo_evento)
        return response

    def delete_tipo_evento_by_id(self, id: int) -> Any:
        return self.tipo_evento_repo.delete_tipo_evento_by_id(id)
