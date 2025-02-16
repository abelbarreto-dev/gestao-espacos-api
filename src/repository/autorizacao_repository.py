from typing import List, Any

from sqlalchemy.orm import Session

from src.core.sql_engine import sync_engine
from src.domain.db.autorizacao import Autorizacao


class AutorizacaoRepository:
    def __init__(self):
        self.engine = sync_engine()

    def create_autorizacao(self, autorizacao: Autorizacao) -> Autorizacao:
        with Session(self.engine) as session:
            session.add(autorizacao)
            session.commit()

        return autorizacao

    def find_all_autorizacaos(self) -> List:
        with Session(self.engine) as session:
            autorizacaos = session.query(Autorizacao).all()

            if not autorizacaos:
                raise Exception("Any Autorizacao Not Found")

        return autorizacaos

    def find_autorizacao_by_id(self, id: int) -> Any:
        with Session(self.engine) as session:
            autorizacao = session.query(Autorizacao).filter_by(id_autorizacao=id).first()

            if not autorizacao:
                raise Exception("Autorizacao Not Found")

        return autorizacao

    def update_autorizacao(self, autorizacao: Autorizacao, id: int) -> Any:
        with Session(self.engine) as session:
            new_autorizacao = session.query(Autorizacao).filter_by(id_autorizacao=id).first()

            if not new_autorizacao:
                raise Exception("Autorizacao Not Found")

            new_autorizacao.id_solicitacao = autorizacao.id_solicitacao
            new_autorizacao.data_emissao = autorizacao.data_emissao
            new_autorizacao.validade = autorizacao.validade

            session.commit()

        return new_autorizacao

    def delete_autorizacao_by_id(self, id: int) -> Any:
        with Session(self.engine) as session:
            autorizacao = session.query(Autorizacao).filter_by(id_autorizacao=id).first()

            if not autorizacao:
                raise Exception("Autorizacao Not Found")

            session.delete(autorizacao)
            session.commit()
