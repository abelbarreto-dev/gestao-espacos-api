from typing import List, Any

from sqlalchemy.orm import Session

from src.core.sql_engine import sync_engine
from src.domain.db.usuario import Usuario


class UsuarioRepository:
    def __init__(self):
        pass

    def create_user(self, user: Usuario) -> Usuario:
        engine = sync_engine()

        with Session(engine) as session:
            session.add(user)
            session.commit()

        return user

    def find_all_users(self) -> List:
        engine = sync_engine()

        with Session(engine) as session:
            all_users = session.query(Usuario).all()

        return all_users

    def find_user_by_id(self, id: int) -> Any:
        engine = sync_engine()

        with Session(engine) as session:
            user = session.query(Usuario).filter_by(id_usuario=id).first()

        return user

    def update_user_nome(self, nome: str, id: int) -> Any:
        engine = sync_engine()

        with Session(engine) as session:
            existing_user = session.query(Usuario).filter_by(id_usuario=id).first()

            if existing_user is None:
                raise Exception("User not found")

            existing_user.nome = nome
            session.commit()

    def update_user_email(self, email: str, id: int) -> Any:
        engine = sync_engine()

        with Session(engine) as session:
            existing_user = session.query(Usuario).filter_by(id_usuario=id).first()

            if existing_user is None:
                raise Exception("User not found")

            existing_user.email = email
            session.commit()

    def update_user_senha(self, senha: str, email: str) -> Any:
        engine = sync_engine()

        with Session(engine) as session:
            existing_user = session.query(Usuario).filter_by(email=email).first()

            if existing_user is None:
                raise Exception("User not found")

            existing_user.senha = senha
            session.commit()

    def delete_user(self, id: int) -> Any:
        engine = sync_engine()

        with Session(engine) as session:
            user = session.query(Usuario).filter_by(id_usuario=id).first()

            if not user:
                raise Exception("User not found")

            session.delete(user)
            session.commit()
