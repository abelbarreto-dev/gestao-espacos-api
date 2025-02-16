from datetime import date

from pydantic import BaseModel


class Autorizacao(BaseModel):
    id_autorizacao: int
    id_solicitacao: int
    data_emissao: date
    validade: date
