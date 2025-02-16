from pydantic import BaseModel


class Usuario(BaseModel):
    id_usuario: int
    nome: str
    email: str
    senha: str
    perfil: str
