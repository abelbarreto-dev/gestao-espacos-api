from typing import Any

from src.domain.db.solicitante import Solicitante as SolicitanteDB
from src.domain.dtos.solicitante import Solicitante
from src.repository.solicitante_repository import SolicitanteRepository
from src.utilities.solicitante_util import SolicitanteUtil


class SolicitanteService:
    def __init__(self):
        self.solicit_repo = SolicitanteRepository()

    def create_solicitante(self, solicitante: Solicitante) -> Any:
        SolicitanteUtil.check_all(solicitante)

        new_solicitante = SolicitanteUtil.to_solicitante_db(solicitante)
        new_solicitante = self.solicit_repo.create_solicitante(new_solicitante)

        response = SolicitanteUtil.from_db_to_base_model(new_solicitante)
        return response

    def find_all_solicitantes(self) -> Any:
        all_solicits = self.solicit_repo.find_all_solicitantes()

        response = SolicitanteUtil.from_db_list_to_base_model(all_solicits)
        return response

    def find_solicitante_by_id(self, id: int) -> Any:
        solicit = self.solicit_repo.find_solicitante_by_id(id)

        response = SolicitanteUtil.from_db_to_base_model(solicit)
        return response

    def update_solicitante_by_id(self, solicitante: SolicitanteDB, id: int) -> Any:
        SolicitanteUtil.check_all(solicitante)

        solicit = self.solicit_repo.update_solicitante_by_id(solicitante, id)

        response = SolicitanteUtil.from_db_to_base_model(solicit)
        return response

    def delete_solicitante_by_id(self, id: int) -> Any:
        return self.solicit_repo.delete_solicitante_by_id(id)
