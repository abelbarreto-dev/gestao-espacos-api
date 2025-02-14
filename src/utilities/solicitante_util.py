from src.domain.db.solicitante import Solicitante as SolicitanteDB
from src.domain.dtos.solicitante import Solicitante


class SolicitanteUtil:
    @classmethod
    def check_all(cls, solicitante: Solicitante | SolicitanteDB) -> None:
        cls.check_nome_length(solicitante.nome)
        cls.check_tipo_length(solicitante.tipo)
        cls.check_documento_length(solicitante.documento)
        cls.check_contanto_length(solicitante.contato)

        cls.check_tipo_value(solicitante.tipo)

    @classmethod
    def check_nome_length(cls, nome: str) -> None:
        if len(nome) > 100:
            raise Exception("Name length over 100 characters")

    @classmethod
    def check_tipo_length(cls, tipo: str) -> None:
        if len(tipo) > 20:
            raise Exception("Tipo length over 20 characters")

    @classmethod
    def check_documento_length(cls, documento: str) -> None:
        if len(documento) > 20:
            raise Exception("Documento length over 20 characters")

    @classmethod
    def check_contanto_length(cls, contanto: str) -> None:
        if len(contanto) > 50:
            raise Exception("Contato length over 50 characters")

    @classmethod
    def check_tipo_value(cls, tipo: str) -> None:
        if tipo not in ("pessoa física", "pessoa jurídica"):
            raise Exception("Tipo must be 'pessoa física' or 'pessoa jurídica'")

    @classmethod
    def to_solicitante_db(cls, solicitante: Solicitante) -> SolicitanteDB:
        solicit_db = SolicitanteDB()

        solicit_db.nome = solicitante.nome
        solicit_db.tipo = solicitante.tipo
        solicit_db.documento = solicitante.documento
        solicit_db.contato = solicitante.contato

        return solicit_db
