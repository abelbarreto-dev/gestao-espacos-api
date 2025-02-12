from datetime import datetime

from datetime import date

from pydantic import BaseModel


class Autorizacao(BaseModel):
    id_solicitacao: int
    data_emissao: datetime
    validade: date
