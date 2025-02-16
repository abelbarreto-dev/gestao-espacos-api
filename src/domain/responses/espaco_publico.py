from typing import Optional

from pydantic import BaseModel


class EspacoPublico(BaseModel):
    id_espaco: int
    nome: str
    endereco: str
    capacidade: int
    disponibilidade: bool
    descricao: Optional[str] = None
