from typing import Any

from src.domain.db.espaco_publico import EspacoPublico as EspacoDB
from src.domain.dtos.espaco_publico import EspacoPublico
from src.repository.espaco_publico_repository import EspacoPublicoRepository
from src.utilities.espaco_publico_util import EspacoPublicoUtil


class EspacoPublicoService:
    def __init__(self) -> None:
        self.esp_pub_repo = EspacoPublicoRepository()

    def create_espaco_publico(self, espaco_publico: EspacoPublico) -> EspacoPublico:
        EspacoPublicoUtil.check_all(espaco_publico)

        new_espaco_publico = EspacoPublicoUtil.to_espaco_publico_db(espaco_publico)
        new_espaco_publico = self.esp_pub_repo.create_espaco_publico(new_espaco_publico)

        response = EspacoPublicoUtil.from_db_to_base_model(new_espaco_publico)
        return response

    def find_all_espaco_publicos(self) -> Any:
        all_esp_pub = self.esp_pub_repo.find_all_espaco_publicos()

        response = EspacoPublicoUtil.from_db_list_to_base_model(all_esp_pub)
        return response

    def find_espaco_publico_by_id(self, id: int) -> EspacoDB:
        esp_pub = self.esp_pub_repo.find_espaco_publico_by_id(id)

        response = EspacoPublicoUtil.from_db_to_base_model(esp_pub)
        return response

    def filter_espaco_publico_by_disponibilidade(self, disponibilidade: bool) -> Any:
        esp_pub = self.esp_pub_repo.filter_espaco_publico_by_disponibilidade(disponibilidade)

        response = EspacoPublicoUtil.from_db_list_to_base_model(esp_pub)
        return response

    def update_espaco_publico(self, espaco_publico: EspacoDB, id: int) -> Any:
        EspacoPublicoUtil.check_all(espaco_publico)

        esp_pub = self.esp_pub_repo.update_espaco_publico(espaco_publico, id)

        response = EspacoPublicoUtil.from_db_to_base_model(esp_pub)
        return response

    def delete_espaco_publico_by_id(self, id: int) -> Any:
        return self.esp_pub_repo.delete_espaco_publico_by_id(id)
