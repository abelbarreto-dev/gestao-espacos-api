from typing import List, Any

from sqlalchemy.orm import Session

from src.core.sql_engine import sync_engine
from src.domain.db.periodo import Periodo


class PeriodoRepository:
    def __init__(self):
        self.engine = sync_engine()

    def create_periodo(self, periodo: Periodo) -> Periodo:
        with Session(self.engine) as session:
            session.add(periodo)
            session.commit()

        return periodo

    def find_all_periodos(self) -> List:
        with Session(self.engine) as session:
            periodos = session.query(Periodo).all()

            if not periodos:
                raise Exception("Any Periodo Found")

        return periodos

    def find_periodo_by_id(self, id_periodo: int) -> Any:
        with Session(self.engine) as session:
            periodo = session.query(Periodo).filter_by(id_periodo=id_periodo).first()

            if not periodo:
                raise Exception("Periodo Not Found")

        return periodo

    def update_periodo(self, periodo: Periodo, id_periodo: int) -> Any:
        with Session(self.engine) as session:
            new_periodo = session.query(Periodo).filter_by(id_periodo=id_periodo).first()

            if not new_periodo:
                raise Exception("Periodo Not Found")

            new_periodo.id_solicitacao = periodo.id_solicitacao
            new_periodo.data_inicio = periodo.data_inicio
            new_periodo.data_fim = periodo.data_fim

            session.commit()

        return new_periodo

    def delete_periodo_by_id(self, id_periodo: int) -> Any:
        with Session(self.engine) as session:
            periodo = session.query(Periodo).filter_by(id_periodo=id_periodo).first()

            if not periodo:
                raise Exception("Periodo Not Found")

            session.delete(periodo)
            session.commit()
