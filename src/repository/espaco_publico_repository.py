from typing import List, Any

from sqlalchemy.orm import Session

from src.core.sql_engine import sync_engine
from src.domain.db.espaco_publico import EspacoPublico


class EspacoPublicoRepository:
    def __init__(self):
        self.engine = sync_engine()

    def create_espaco_publico(self, espaco_publico: EspacoPublico) -> EspacoPublico:
        with Session(self.engine) as session:
            session.add(espaco_publico)
            session.commit()

        return espaco_publico

    def find_all_espaco_publicos(self) -> List:
        with Session(self.engine) as session:
            all_espacos_publicos = session.query(EspacoPublico).all()

        if not all_espacos_publicos:
            raise Exception("Espaço Público not found")

        return all_espacos_publicos

    def find_espaco_publico_by_id(self, id: int) -> EspacoPublico:
        with Session(self.engine) as session:
            espaco_publico = session.query(EspacoPublico).filter_by(id_usuario=id).first()

        if not espaco_publico:
            raise Exception("Espaço Público not found")

        return espaco_publico()

    def update_espaco_publico(self, espaco_publico: EspacoPublico, id: int) -> EspacoPublico:
        with Session(self.engine) as session:
            new_esp_publico = session.query(EspacoPublico).filter_by(id_espaco=id).first()

            if not new_esp_publico:
                raise Exception("Espaço Público not found")

            new_esp_publico.nome = espaco_publico.nome
            new_esp_publico.endereco = espaco_publico.endereco
            new_esp_publico.descricao = espaco_publico.descricao
            new_esp_publico.capacidade = espaco_publico.capacidade
            new_esp_publico.disponibilidade = espaco_publico.disponibilidade

            session.commit()

        return new_esp_publico()

    def delete_espaco_publico_by_id(self, id: int) -> Any:
        with Session(self.engine) as session:
            espaco_publico = session.query(EspacoPublico).filter_by(id_espaco=id).first()

            if not espaco_publico:
                raise Exception("Espaço Público not found")

            session.delete(espaco_publico)
            session.commit()
