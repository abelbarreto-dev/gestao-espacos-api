from datetime import datetime

from src.domain.db.solicitacao import Solicitacao as SolicitacaoDB
from src.domain.dtos.solicitacao import Solicitacao


class SolicitacaoUtil:
    @classmethod
    def check_all(cls, solicitacao: Solicitacao | SolicitacaoDB) -> None:
        cls.check_status(solicitacao.status)
        cls.check_datetime(solicitacao.data_solicitacao)

    @classmethod
    def check_status(cls, status: str) -> None:
        if status not in ("pendente", "aprovado", "negado"):
            raise Exception(f"{status} is not a valid status")

    @classmethod
    def check_datetime(cls, datetime_value: datetime) -> None:
        format_date = "%Y-%m-%d %H:%M:%S"
        str_datetime = str(datetime_value)

        try:
            datetime.strptime(str_datetime, format_date)
        except ValueError:
            raise Exception(f"{str_datetime} is not a valid datetime")
