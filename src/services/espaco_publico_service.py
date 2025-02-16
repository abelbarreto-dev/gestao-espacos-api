from typing import List, Any

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
        return self.esp_pub_repo.create_espaco_publico(new_espaco_publico)

    def find_all_espaco_publicos(self) -> List:
        return self.esp_pub_repo.find_all_espaco_publicos()

    def find_espaco_publico_by_id(self, id: int) -> EspacoDB:
        return self.esp_pub_repo.find_espaco_publico_by_id(id)

    def filter_espaco_publico_by_disponibilidade(self, disponibilidade: bool) -> List:
        return self.esp_pub_repo.filter_espaco_publico_by_disponibilidade(disponibilidade)

    def update_espaco_publico(self, espaco_publico: EspacoDB, id: int) -> EspacoDB:
        EspacoPublicoUtil.check_all(espaco_publico)

        return self.esp_pub_repo.update_espaco_publico(espaco_publico, id)

    def delete_espaco_publico_by_id(self, id: int) -> Any:
        return self.esp_pub_repo.delete_espaco_publico_by_id(id)
