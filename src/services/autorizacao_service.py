from typing import Any

from src.domain.db.autorizacao import Autorizacao as AutorizacaoDB
from src.domain.dtos.autorizacao import Autorizacao
from src.repository.autorizacao_repository import AutorizacaoRepository
from src.utilities.autorizacao_util import AutorizacaoUtil


class AutorizacaoService:
    def __init__(self):
        self.auth_repo = AutorizacaoRepository()

    def create_autorizacao(self, autorizacao: Autorizacao) -> Autorizacao:
        AutorizacaoUtil.check_all(autorizacao)

        autorizacao_db = AutorizacaoUtil.to_autorizacao_db(autorizacao)
        autorizacao_db = self.auth_repo.create_autorizacao(autorizacao_db)

        response = AutorizacaoUtil.from_db_to_base_model(autorizacao_db)
        return response

    def find_all_autorizacaos(self) -> Any:
        all_autorize = self.auth_repo.find_all_autorizacaos()

        response = AutorizacaoUtil.from_db_list_to_base_model(all_autorize)
        return response

    def find_autorizacao_by_id(self, id: int) -> Any:
        autorizacao = self.auth_repo.find_autorizacao_by_id(id)

        response = AutorizacaoUtil.from_db_to_base_model(autorizacao)
        return response

    def update_autorizacao(self, autorizacao: AutorizacaoDB, id: int) -> Any:
        AutorizacaoUtil.check_all(autorizacao)

        autorizacao = self.auth_repo.update_autorizacao(autorizacao, id)

        response = AutorizacaoUtil.from_db_to_base_model(autorizacao)
        return response

    def delete_autorizacao_by_id(self, id: int) -> Any:
        return self.auth_repo.delete_autorizacao_by_id(id)
