from pydantic import BaseModel


class TipoEvento(BaseModel):
    descricao: str
