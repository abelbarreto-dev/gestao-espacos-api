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
        new_solicitacao = self.solicit_repo.create_solicitacao(new_solicitacao)

        response = SolicitacaoUtil.from_db_to_base_model(new_solicitacao)
        return response

    def find_all_solicitacaos(self) -> List:
        all_solicits = self.solicit_repo.find_all_solicitacaos()

        response = SolicitacaoUtil.from_db_list_to_base_model(all_solicits)
        return response

    def find_solicitacao_by_id(self, id: int) -> Any:
        solicit = self.solicit_repo.find_solicitacao_by_id(id)

        response = SolicitacaoUtil.from_db_to_base_model(solicit)
        return response

    def filter_solicitacao_by_status(self, status: str) -> List:
        SolicitacaoUtil.check_status(status)

        solicit = self.solicit_repo.find_solicitacao_by_status(status)

        response = SolicitacaoUtil.from_db_list_to_base_model(solicit)
        return response

    def filter_solicitacao_by_solicitante_id(self, solicitante_id: int) -> List:
        solicit = self.solicit_repo.filter_solicitacao_by_solicitante_id(solicitante_id)

        response = SolicitacaoUtil.from_db_list_to_base_model(solicit)
        return response

    def update_solicitacao(self, solicitacao: SolicitacaoDB, id: int) -> Any:
        SolicitacaoUtil.check_all(solicitacao)

        solicit = self.solicit_repo.update_solicitacao(solicitacao, id)

        response = SolicitacaoUtil.from_db_to_base_model(solicit)
        return response

    def delete_solicitacao_by_id(self, id: int) -> Any:
        return self.solicit_repo.delete_solicitacao_by_id(id)
