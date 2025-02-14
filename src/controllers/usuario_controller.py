from typing import Any

from src.domain.dtos.usuario import Usuario
from src.exceptions.http_exception import HTTPError
from src.services.usuario_service import UsuarioService


class UsuarioController:
    def __init__(self):
        self.user_service = UsuarioService()

    def create_user(self, user: Usuario) -> Any:
        try:
            return self.user_service.create_user(user)
        except Exception as e:
            raise HTTPError(str(e))

    def find_all_users(self) -> Any:
        try:
            return self.user_service.find_all_users()
        except Exception as e:
            raise HTTPError(str(e))

    def find_user_by_id(self, id: int) -> Any:
        try:
            return self.user_service.find_user_by_id(id)
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
