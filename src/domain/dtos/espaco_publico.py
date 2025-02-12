from pydantic import BaseModel


class EspacoPublico(BaseModel):
    nome: str
    endereco: str
    descricao: str
    capacidade: int
    disponibilidade: bool = True
