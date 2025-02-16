from typing import List

from src.domain.db.espaco_publico import EspacoPublico as EspacoDB
from src.domain.dtos.espaco_publico import EspacoPublico
from src.domain.responses.espaco_publico import EspacoPublico as ResponseEspaco


class EspacoPublicoUtil:
    @classmethod
    def check_all(cls, espaco_publico: EspacoPublico | EspacoDB) -> None:
        cls.check_nome_length(espaco_publico.nome)
        cls.check_endereco_length(espaco_publico.endereco)
        cls.check_capacidade_length(espaco_publico.capacidade)

    @classmethod
    def check_nome_length(cls, nome: str) -> None:
        if len(nome) > 100:
            raise Exception("Name length over 100 characters")

    @classmethod
    def check_endereco_length(cls, endereco: str) -> None:
        if len(endereco) > 100:
            raise Exception("Endereco length over 100 characters")

    @classmethod
    def check_capacidade_length(cls, capacidade: int) -> None:
        if capacidade < 0:
            raise Exception("Capacidade length cannot be negative or zero")

    @classmethod
    def to_espaco_publico_db(cls, espaco_publico: EspacoPublico) -> EspacoDB:
        espaco_db = EspacoDB()

        espaco_db.nome = espaco_publico.nome
        espaco_db.endereco = espaco_publico.endereco
        espaco_db.descricao = espaco_publico.descricao
        espaco_db.capacidade = espaco_publico.capacidade
        espaco_db.disponibilidade = espaco_publico.disponibilidade

        return espaco_db

    @classmethod
    def from_db_to_base_model(cls, espaco_publico: EspacoDB) -> ResponseEspaco:
        return ResponseEspaco(
            id_espaco=espaco_publico.id_espaco,
            nome=espaco_publico.nome,
            endereco=espaco_publico.endereco,
            capacidade=espaco_publico.capacidade,
            disponibilidade=espaco_publico.disponibilidade,
            descricao=espaco_publico.descricao
        )

    @classmethod
    def from_db_list_to_base_model(cls, espacos_publicos: List[EspacoDB]) -> List[ResponseEspaco]:
        return [
            cls.from_db_to_base_model(espaco)
            for espaco in espacos_publicos
        ]
