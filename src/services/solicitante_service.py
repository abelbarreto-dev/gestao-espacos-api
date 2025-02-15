from typing import List, Any

from src.domain.db.solicitante import Solicitante as SolicitanteDB
from src.domain.dtos.solicitante import Solicitante
from src.repository.solicitante_repository import SolicitanteRepository
from src.utilities.solicitante_util import SolicitanteUtil


class SolicitanteService:
    def __init__(self):
        self.solicit_repo = SolicitanteRepository()

    def create_solicitante(self, solicitante: Solicitante) -> Solicitante:
        SolicitanteUtil.check_all(solicitante)

        new_solicitante = SolicitanteUtil.to_solicitante_db(solicitante)
        return self.solicit_repo.create_solicitante(new_solicitante)

    def find_all_solicitantes(self) -> List:
        return self.solicit_repo.find_all_solicitantes()

    def find_solicitante_by_id(self, id: int) -> SolicitanteDB:
        return self.solicit_repo.find_solicitante_by_id(id)

    def update_solicitante_by_id(self, solicitante: SolicitanteDB, id: int) -> SolicitanteDB:
        SolicitanteUtil.check_all(solicitante)

        return self.solicit_repo.update_solicitante_by_id(solicitante, id)

    def delete_solicitante_by_id(self, id: int) -> Any:
        return self.solicit_repo.delete_solicitante_by_id(id)
