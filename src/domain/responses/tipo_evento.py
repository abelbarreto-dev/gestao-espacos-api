from typing import Optional

from pydantic import BaseModel


class TipoEvento(BaseModel):
    id_tipo_evento: int
    descricao: Optional[str] = None
