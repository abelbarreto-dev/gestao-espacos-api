from typing import Any

from fastapi.routing import APIRouter

from src.controllers.periodo_controller import PeriodoController
from src.domain.dtos.periodo import Periodo


periodo_controller = PeriodoController()
periodo_routes = APIRouter()


@periodo_routes.post("/periodos")
def create_periodo(periodo: Periodo) -> Any:
    return periodo_controller.create_periodo(periodo)


@periodo_routes.get("/periodos")
def find_all_periodos() -> Any:
    return periodo_controller.find_all_periodos()


@periodo_routes.get("/periodos/{id}")
def find_periodo_by_id(id: int) -> Any:
    return periodo_controller.find_periodo_by_id(id)


@periodo_routes.put("/periodos/{id}")
def update_periodo(periodo: dict, id: int) -> Any:
    return periodo_controller.update_periodo(periodo, id)


@periodo_routes.delete("/periodos/{id}")
def delete_periodo_by_id(id: int) -> Any:
    return periodo_controller.delete_periodo_by_id(id)
