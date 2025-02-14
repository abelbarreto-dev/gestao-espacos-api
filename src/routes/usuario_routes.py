from typing import Any

from fastapi import APIRouter

from src.controllers.usuario_controller import UsuarioController
from src.domain.dtos.extra.email_dto import EmailDto
from src.domain.dtos.extra.login_dto import LoginDto
from src.domain.dtos.extra.nome_dto import NomeDto
from src.domain.dtos.usuario import Usuario


user_router_api = APIRouter()
user_controller = UsuarioController()


@user_router_api.post("/usuarios")
def create_user(user: Usuario) -> Any:
    return user_controller.create_user(user)


@user_router_api.get("/usuarios")
def find_all_users() -> Any:
    return user_controller.find_all_users()


@user_router_api.get("/usuarios/{id}")
def find_user_by_id(id: int) -> Any:
    return user_controller.find_user_by_id(id)


@user_router_api.patch("/usuarios/update-nome/{id}")
def update_user_nome(nome: NomeDto, id: int) -> Any:
    return user_controller.update_user_nome(nome.nome, id)


@user_router_api.patch("/usuarios/update-email/{id}")
def update_user_email(email: EmailDto, id: int) -> Any:
    return user_controller.update_user_email(email.email, id)


@user_router_api.patch("/usuarios/recovery-senha")
def update_user_senha(recovery: LoginDto) -> Any:
    return user_controller.update_user_senha(
        recovery.senha,
        recovery.email
    )


@user_router_api.delete("/delete/{id}")
def delete_user(id: int) -> Any:
    return user_controller.delete_user(id)
