from datetime import date

from src.domain.db.autorizacao import Autorizacao as AutorizacaoDB
from src.domain.dtos.autorizacao import Autorizacao


class AutorizacaoUtil:
    @classmethod
    def check_all(cls, autorizacao: Autorizacao | AutorizacaoDB) -> None:
        cls.check_date_instance(autorizacao.validade)
        cls.check_date_instance(autorizacao.data_emissao)

    @classmethod
    def check_date_instance(cls, date_instance: any) -> None:
        if not date_instance or not isinstance(date_instance, date):
            raise Exception("Date value is null or invalid instance")

    @classmethod
    def to_autorizacao_db(cls, autorizacao: Autorizacao) -> AutorizacaoDB:
        author_db = AutorizacaoDB()

        author_db.id_solicitacao = autorizacao.id_solicitacao
        author_db.data_emissao = autorizacao.data_emissao
        author_db.validade = autorizacao.validade

        return author_db
