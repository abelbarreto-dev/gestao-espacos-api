from typing import Any, List

from sqlalchemy.orm import Session

from src.core.sql_engine import sync_engine
from src.domain.db.solicitante import Solicitante


class SolicitanteRepository:
    def __init__(self):
        self.engine = sync_engine()

    def create_solicitante(self, solicitante: Solicitante) -> Solicitante:
        with Session(self.engine) as session:
            session.add(solicitante)
            session.commit()

        return solicitante

    def find_all_solicitantes(self) -> List:
        with Session(self.engine) as session:
            all_solicitantes = session.query(Solicitante).all()

        if not all_solicitantes:
            raise Exception("No solicitantes found")

        return all_solicitantes

    def find_solicitante_by_id(self, id: int) -> Solicitante:
        with Session(self.engine) as session:
            solicitante = session.query(Solicitante).filter_by(id_solicitante=id).first()

        if not solicitante:
            raise Exception("No solicitante found")

        return solicitante()

    def update_solicitante_by_id(self, solicitante: Solicitante, id: int) -> Solicitante:
        with Session(self.engine) as session:
            new_solicitante = session.query(Solicitante).filter_by(id_solicitante=id).first()

            if not new_solicitante:
                raise Exception("No solicitante found")

            new_solicitante.nome = solicitante.nome
            new_solicitante.tipo = solicitante.tipo
            new_solicitante.documento = solicitante.documento
            new_solicitante.contato = solicitante.contato

            session.commit()

        return new_solicitante()

    def delete_solicitante_by_id(self, id: int) -> Any:
        with Session(self.engine) as session:
            solicitante = session.query(Solicitante).filter_by(id_solicitante=id).first()

            if not solicitante:
                raise Exception("No solicitante found")

            session.delete(solicitante)
            session.commit()
