from pydantic import BaseModel


class Solicitante(BaseModel):
    id_solicitante: int
    nome: str
    tipo: str
    documento: str
    contato: str
