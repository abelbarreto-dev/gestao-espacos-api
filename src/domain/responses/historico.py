from datetime import datetime

from pydantic import BaseModel


class Historico(BaseModel):
    id_historico: int
    id_solicitacao: int
    usuario_responsavel: int
    campo_modificado: str
    valor_anterior: str
    valor_novo: str
    data_modificacao: datetime = datetime.now()
