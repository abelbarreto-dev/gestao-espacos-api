from pydantic import BaseModel


class UserDTO(BaseModel):
    nome: str
    email: str
    senha: str
    perfil: str
