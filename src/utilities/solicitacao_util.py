from typing import List

from src.domain.db.solicitacao import Solicitacao as SolicitacaoDB
from src.domain.dtos.solicitacao import Solicitacao
from src.domain.responses.solicitacao import Solicitacao as SolicitacaoResponse


class SolicitacaoUtil:
    @classmethod
    def check_all(cls, solicitacao: Solicitacao | SolicitacaoDB) -> None:
        cls.check_status(solicitacao.status)

    @classmethod
    def check_status(cls, status: str) -> None:
        if status not in ("pendente", "aprovado", "negado"):
            raise Exception(f"{status} is not a valid status")

    @classmethod
    def to_solicitacao_db(cls, solicitacao: Solicitacao) -> SolicitacaoDB:
        solicit_db = SolicitacaoDB()

        solicit_db.id_solicitante = solicitacao.id_solicitante
        solicit_db.id_usuario = solicitacao.id_usuario
        solicit_db.id_espaco = solicitacao.id_espaco
        solicit_db.id_tipo_evento = solicitacao.id_tipo_evento
        solicit_db.status = solicitacao.status
        solicit_db.data_solicitacao = solicitacao.data_solicitacao

        return solicit_db

    @classmethod
    def from_db_to_base_model(cls, solicia_db: SolicitacaoDB) -> SolicitacaoResponse:
        return SolicitacaoResponse(
            id_solicitacao=solicia_db.id_solicitante,
            id_solicitante=solicia_db.id_solicitante,
            id_usuario=solicia_db.id_usuario,
            id_espaco=solicia_db.id_espaco,
            id_tipo_evento=solicia_db.id_tipo_evento,
            status=solicia_db.status
        )

    @classmethod
    def from_db_list_to_base_model(cls, solicias_db: List[SolicitacaoDB]) -> List[SolicitacaoResponse]:
        return [
            cls.to_solicitacao_db(solicit)
            for solicit in solicias_db
        ]
