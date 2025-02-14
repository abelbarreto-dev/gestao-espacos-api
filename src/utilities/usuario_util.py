from re import match

from src.domain.dtos.usuario import Usuario
from src.domain.db.usuario import Usuario as UserDB


regex_email = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"


class UsuarioUtil:
    @classmethod
    def check_all(cls, usuario: Usuario):
        cls.check_nome_length(usuario.nome)
        cls.check_email_length(usuario.email)
        cls.check_perfil_length(usuario.perfil)
        cls.check_senha_length(usuario.senha)

        if usuario.perfil not in ("administrador", "solicitante"):
            raise Exception("Perfil must be 'administrador' or 'solicitante'")

        if not cls.check_email(usuario.email):
            raise Exception("Email must be valid")

    @classmethod
    def check_nome_length(cls, nome: str) -> None:
        if len(nome) > 100:
            raise Exception("Name length over 100 characters")

    @classmethod
    def check_email_length(cls, email: str) -> None:
        if len(email) > 100:
            raise Exception("Email length over 100 characters")

    @classmethod
    def check_perfil_length(cls, perfil: str) -> None:
        if len(perfil) > 100:
            raise Exception("Perfil length over 20 characters")

    @classmethod
    def check_senha_length(cls, senha: str) -> None:
        if len(senha) < 6:
            raise Exception("Senha length must at least 6 characters")

    @classmethod
    def check_email(cls, email: str) -> bool:
        invalid = not match(regex_email, email)

        return not invalid

    @classmethod
    def to_user_db(cls, user: Usuario) -> UserDB:
        user_db = UserDB()

        user_db.nome = user.nome
        user_db.email = user.email
        user_db.perfil = user.perfil
        user_db.senha = user.senha

        return user_db
