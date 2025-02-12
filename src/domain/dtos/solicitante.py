from pydantic import BaseModel


class Solicitante(BaseModel):
    nome: str
    tipo: str
    documento: str
    contato: str
