from typing import List, Any

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
        return self.auth_repo.create_autorizacao(autorizacao_db)

    def find_all_autorizacaos(self) -> List:
        return self.auth_repo.find_all_autorizacaos()

    def find_all_autorizacao_by_id(self, id: int) -> Any:
        return self.auth_repo.find_autorizacao_by_id(id)

    def update_autorizacao(self, autorizacao: AutorizacaoDB, id: int) -> Any:
        AutorizacaoUtil.check_all(autorizacao)

        return self.auth_repo.update_autorizacao(autorizacao, id)

    def delete_autorizacao_by_id(self, id: int) -> Any:
        return self.auth_repo.delete_autorizacao_by_id(id)
