from typing import List, Any

from sqlalchemy.exc import NoResultFound

from src.domain.dtos.extra.login_dto import LoginDto
from src.domain.dtos.usuario import Usuario
from src.repository.usuario_repository import UsuarioRepository
from src.utilities.usuario_util import UsuarioUtil


class UsuarioService:
    def __init__(self):
        self.user_repo = UsuarioRepository()

    def create_user(self, user: Usuario) -> Usuario:
        UsuarioUtil.check_all(user)

        new_user = UsuarioUtil.to_user_db(user)
        db_user = self.user_repo.create_user(new_user)
        new_user = UsuarioUtil.from_db_to_base_model(db_user)

        return new_user

    def find_user_make_login(self, login: LoginDto) -> Any:
        user = self.user_repo.find_user_make_login(login)

        new_user = UsuarioUtil.from_db_to_base_model(user)

        return new_user

    def update_user_nome(self, nome: str, id: int) -> Any:
        UsuarioUtil.check_nome_length(nome)

        return self.user_repo.update_user_nome(nome, id)

    def update_user_email(self, email: str, id: int) -> Any:
        UsuarioUtil.check_email(email)

        return self.user_repo.update_user_email(email, id)

    def update_user_senha(self, senha: str, email: str) -> Any:
        UsuarioUtil.check_senha_length(senha)

        return self.user_repo.update_user_senha(senha, email)

    def delete_user(self, id: int) -> Any:
        return self.user_repo.delete_user(id)
