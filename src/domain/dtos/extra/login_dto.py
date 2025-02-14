from pydantic import BaseModel


class LoginDto(BaseModel):
    email: str
    senha: str
