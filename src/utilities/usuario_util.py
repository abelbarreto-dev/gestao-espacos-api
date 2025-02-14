from re import match

from src.domain.dtos.usuario import Usuario
from src.domain.db.usuario import Usuario as UserDB


regex_email = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"


class UsuarioUtil:
    @classmethod
    def check_all(cls, usuario: Usuario):
        if len(usuario.nome) > 100:
            raise Exception("Name length over 100 characters")
        if len(usuario.email) > 100:
            raise Exception("Email length over 100 characters")
        if len(usuario.perfil) > 20:
            raise Exception("Perfil length over 20 characters")

        if usuario.perfil not in ("administrador", "solicitante"):
            raise Exception("Perfil must be 'administrador' or 'solicitante'")

        if len(usuario.senha) < 6:
            raise Exception("Senha length must at least 6 characters")

        if not cls.check_email(usuario.email):
            raise Exception("Email must be valid")

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
