from datetime import date
from typing import List

from src.domain.db.autorizacao import Autorizacao as AutorizacaoDB
from src.domain.dtos.autorizacao import Autorizacao
from src.domain.responses.autorizacao import Autorizacao as AutorizacaoResponse


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

    @classmethod
    def from_db_to_base_model(cls, autorizacao: AutorizacaoDB) -> AutorizacaoResponse:
        return AutorizacaoResponse(
            id_autorizacao=autorizacao.id_autorizacao,
            id_solicitacao=autorizacao.id_solicitacao,
            data_emissao=autorizacao.data_emissao,
            validade=autorizacao.validade
        )

    @classmethod
    def from_db_list_to_base_model(cls, autorizacoes: List[Autorizacao]) -> List[AutorizacaoResponse]:
        return [
            cls.from_db_to_base_model(autorizacao)
            for autorizacao in autorizacoes
        ]
