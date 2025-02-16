from src.domain.db.tipo_evento import TipoEvento as TipoEventoDB
from src.domain.dtos.tipo_evento import TipoEvento
from src.domain.responses.tipo_evento import TipoEvento as TipoEventoResponse


class TipoEventoUtil:
    @classmethod
    def check_all(cls, tipo_evento: TipoEvento) -> None:
        cls.check_description_length(tipo_evento.descricao)

    @classmethod
    def check_description_length(cls, descricao: str) -> None:
        if len(descricao) > 100:
            raise Exception("Descricao length over 100 characters")

    @classmethod
    def to_tipo_evento_db(cls, tipo_evento: TipoEvento) -> TipoEventoDB:
        tipo_ev_db = TipoEventoDB()

        tipo_ev_db.descricao = tipo_evento.descricao

        return tipo_ev_db

    @classmethod
    def from_db_to_base_model(cls, tipo_evento: TipoEventoDB) -> TipoEventoResponse:
        return TipoEventoResponse(
            id_tipo_evento=tipo_evento.id_tipo_evento,
            descricao=tipo_evento.descricao
        )
