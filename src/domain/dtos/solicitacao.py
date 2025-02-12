from datetime import datetime

from pydantic import BaseModel


class Solicitacao(BaseModel):
    id_solicitante: int
    id_usuario: int
    id_espaco: int
    id_tipo_evento: int
    status: str
    data_solicitacao: datetime
