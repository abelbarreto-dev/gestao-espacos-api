from typing import Any

from src.domain.dtos.extra.login_dto import LoginDto
from src.domain.dtos.usuario import Usuario
from src.exceptions.http_exception import HTTPError
from src.response.response import response_builder
from src.services.usuario_service import UsuarioService


class UsuarioController:
    def __init__(self):
        self.user_service = UsuarioService()

    def create_user(self, user: Usuario) -> Any:
        try:
            new_user = self.user_service.create_user(user)

            return response_builder(data=new_user.model_dump())
        except Exception as e:
            raise HTTPError(str(e))

    def find_user_make_login(self, login: LoginDto) -> Any:
        try:
            user = self.user_service.find_user_make_login(login)

            return response_builder(data=user.model_dump())
        except Exception as e:
            raise HTTPError(str(e))

    def update_user_nome(self, nome: str, id: int) -> Any:
        try:
            return self.user_service.update_user_nome(nome, id)
        except Exception as e:
            raise HTTPError(str(e))

    def update_user_email(self, email: str, id: int) -> Any:
        try:
            return self.user_service.update_user_email(email, id)
        except Exception as e:
            raise HTTPError(str(e))

    def update_user_senha(self, senha: str, email: str) -> Any:
        try:
            return self.user_service.update_user_senha(senha, email)
        except Exception as e:
            raise HTTPError(str(e))

    def delete_user(self, id: int) -> Any:
        try:
            return self.user_service.delete_user(id)
        except Exception as e:
            raise HTTPError(str(e))
