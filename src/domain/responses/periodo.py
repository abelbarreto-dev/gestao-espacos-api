from datetime import datetime

from pydantic import BaseModel


class Periodo(BaseModel):
    id_periodo: int
    id_solicitacao: int
    data_inicio: datetime
    data_fim: datetime
