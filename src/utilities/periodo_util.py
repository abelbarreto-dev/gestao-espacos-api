from datetime import datetime

from src.domain.db.periodo import Periodo as PeriodoDB
from src.domain.dtos.periodo import Periodo


class PeriodoUtil:
    @classmethod
    def check_all(cls, periodo: Periodo | PeriodoDB):
        cls.check_dates(periodo.data_inicio, periodo.data_fim)

    @classmethod
    def check_dates(cls, date_init: datetime, date_end: datetime) -> None:
        if date_end <= date_init:
            raise Exception("End date must be before start date")

    @classmethod
    def to_periodo_db(cls, periodo: Periodo) -> PeriodoDB:
        periodo_db = PeriodoDB()

        periodo_db.id_solicitacao = periodo.id_solicitacao
        periodo_db.data_inicio = periodo.data_inicio
        periodo_db.data_fim = periodo.data_fim

        return periodo_db
