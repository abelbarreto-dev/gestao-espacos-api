from pydantic import BaseModel


class NomeDto(BaseModel):
    nome: str
