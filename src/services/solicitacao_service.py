from datetime import datetime
from typing import List, Any

from src.domain.db.solicitacao import Solicitacao as SolicitacaoDB
from src.domain.dtos.solicitacao import Solicitacao
from src.repository.solicitacao_repository import SolicitacaoRepository
from src.utilities.solicitacao_util import SolicitacaoUtil


class SolicitacaoService:
    def __init__(self):
        self.solicit_repo = SolicitacaoRepository()

    def create_solicitacao(self, solicitaco: Solicitacao) -> Solicitacao:
        solicitaco.data_solicitacao = datetime.now()
        SolicitacaoUtil.check_all(solicitaco)

        new_solicitacao = SolicitacaoUtil.to_solicitacao_db(solicitaco)
        return self.solicit_repo.create_solicitacao(new_solicitacao)

    def find_all_solicitacaos(self) -> List:
        return self.solicit_repo.find_all_solicitacaos()

    def find_solicitacao_by_id(self, id: int) -> Any:
        return self.solicit_repo.find_solicitacao_by_id(id)

    def filter_solicitacao_by_status(self, status: str) -> List:
        SolicitacaoUtil.check_status(status)

        return self.solicit_repo.find_solicitacao_by_status(status)

    def filter_solicitacao_by_solicitante_id(self, solicitante_id: int) -> List:
        return self.solicit_repo.filter_solicitacao_by_solicitante_id(solicitante_id)

    def update_solicitacao(self, solicitacao: SolicitacaoDB, id: int) -> Any:
        SolicitacaoUtil.check_all(solicitacao)

        return self.solicit_repo.update_solicitacao(solicitacao, id)

    def delete_solicitacao_by_id(self, id: int) -> Any:
        return self.solicit_repo.delete_solicitacao_by_id(id)
