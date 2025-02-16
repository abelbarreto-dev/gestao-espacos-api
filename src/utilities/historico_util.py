from datetime import datetime

from src.domain.db.historico import Historico as HistoricoDB
from src.domain.dtos.historico import Historico
from src.domain.responses.historico import Historico as HistoricoResponse


class HistoricoUtil:
    @classmethod
    def check_all(cls, historico: Historico | HistoricoDB) -> None:
        cls.check_datetime_instance(historico.data_modificacao)
        cls.check_campo_modificado(historico.campo_modificado)

    @classmethod
    def check_datetime_instance(cls, datetime_instance: any) -> None:
        if not datetime_instance or not isinstance(datetime_instance, datetime):
            raise Exception("DateTime value is null or invalid instance")

    @classmethod
    def check_campo_modificado(cls, campo_mod: str) -> None:
        if not campo_mod or len(campo_mod) > 100:
            raise Exception(f"Campo modificado can't be longer than 100 characters")

    @classmethod
    def to_historico_db(cls, historico: Historico) -> HistoricoDB:
        story = HistoricoDB()

        story.id_solicitacao = historico.id_solicitacao
        story.usuario_responsavel = historico.usuario_responsavel
        story.campo_modificado = historico.campo_modificado
        story.valor_anterior = historico.valor_anterior
        story.valor_novo = historico.valor_novo
        story.data_modificacao = historico.data_modificacao

        return story

    @classmethod
    def from_db_to_base_model(cls, historico_db: HistoricoDB) -> HistoricoResponse:
        return HistoricoResponse(
            id_historico=historico_db.id_historico,
            id_solicitacao=historico_db.id_solicitacao,
            usuario_responsavel=historico_db.usuario_responsavel,
            campo_modificado=historico_db.campo_modificado,
            valor_anterior=historico_db.valor_anterior,
            valor_novo=historico_db.valor_novo,
        )
