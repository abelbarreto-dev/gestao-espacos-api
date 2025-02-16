from typing import List, Any

from sqlalchemy.orm import Session

from src.core.sql_engine import sync_engine
from src.domain.db.historico import Historico


class HistoricoRepository:
    def __init__(self):
        self.engine = sync_engine()

    def create_historico(self, historico) -> Historico:
        with Session(self.engine) as session:
            session.add(historico)
            session.commit()

        return historico

    def find_all_historicos(self) -> List:
        with Session(self.engine) as session:
            historicos = session.query(Historico).all()

            if not historicos:
                raise Exception("Any Historico Not Found")

        return historicos

    def find_historico_by_id(self, id: int) -> Any:
        with Session(self.engine) as session:
            historico = session.query(Historico).filter_by(id_historico=id).first()

            if not historico:
                raise Exception("Historico Not Found")

        return historico

    def filter_historico_by_solicitacao_id(self, solicitacao_id: int) -> List:
        with Session(self.engine) as session:
            historicos = session.query(Historico).filter_by(id_solicitacao=solicitacao_id).all()

            if not historicos:
                raise Exception("Any Historico Not Found")

        return historicos

    def update_historico(self, historico: Historico, id: int) -> Any:
        with Session(self.engine) as session:
            new_historico = session.query(Historico).filter_by(id_historico=id).first()

            if not new_historico:
                raise Exception("Historico Not Found")

            new_historico.id_solicitacao = historico.id_solicitacao
            new_historico.usuario_responsavel = historico.usuario_responsavel
            new_historico.campo_modificado = historico.campo_modificado
            new_historico.valor_anterior = historico.valor_anterior
            new_historico.valor_novo = historico.valor_novo
            new_historico.data_modificacao = historico.data_modificacao

            session.commit()

        return new_historico

    def delete_historico_by_id(self, id: int) -> Any:
        with Session(self.engine) as session:
            historico = session.query(Historico).filter_by(id_historico=id).first()

            if not historico:
                raise Exception("Historico Not Found")

            session.delete(historico)
            session.commit()
