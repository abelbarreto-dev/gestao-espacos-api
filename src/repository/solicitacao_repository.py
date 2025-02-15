from typing import List

from sqlalchemy.orm import Session

from src.core.sql_engine import sync_engine
from src.domain.db.solicitacao import Solicitacao


class SolicitacaoRepository:
    def __init__(self):
        self.engine = sync_engine()

    def create_solicitacao(self, solicitaco: Solicitacao) -> Solicitacao:
        with Session(self.engine) as session:
            session.add(solicitaco)
            session.commit()

        return solicitaco

    def find_all_solicitacaos(self) -> List:
        with Session(self.engine) as session:
            solicitacaos = session.query(Solicitacao).all()

            if not solicitacaos:
                raise Exception("Any solicitacao not found")

        return solicitacaos

    def find_solicitacao_by_id(self, id: int) -> Any:
        with Session(self.engine) as session:
            solicitacao = session.query(Solicitacao).filter_by(id_solicitacao=id).first()

            if not solicitacao:
                raise Exception("Solicitacao not found")

        return solicitacao

    def update_solicitacao(self, solicitacao: Solicitacao, id: int) -> Any:
        with Session(self.engine) as session:
            new_solicitacao = session.query(Solicitacao).filter_by(id_solicitacao=id).first()

            if not new_solicitacao:
                raise Exception("Solicitacao not found")

            new_solicitacao.id_solicitante = solicitacao.id_solicitante
            new_solicitacao.id_usuario = solicitacao.id_usuario
            new_solicitacao.id_espaco = solicitacao.id_espaco
            new_solicitacao.id_tipo_evento = solicitacao.id_tipo_evento

            new_solicitacao.status = solicitacao.status

            new_solicitacao.data_solicitacao = solicitacao.data_solicitacao

            session.commit()

        return new_solicitacao

    def delete_solicitacao_by_id(self, id: int) -> Any:
        with Session(self.engine) as session:
            solicitacao = session.query(Solicitacao).filter_by(id_solicitacao=id).first()

            if not solicitacao:
                raise Exception("Solicitacao not found")

            session.delete(solicitacao)
            session.commit()
