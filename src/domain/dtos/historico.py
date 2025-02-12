from datetime import datetime

from typing import Optional

from pydantic import BaseModel


class Historico(BaseModel):
    id_solicitacao: int
    usuario_responsavel: int
    campo_modificado: str
    valor_anterior: Optional[str] = None
    valor_novo: Optional[str] = None
    data_modificacao: datetime
