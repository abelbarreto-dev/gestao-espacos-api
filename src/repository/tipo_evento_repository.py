from typing import List, Any

from sqlalchemy.orm import Session

from src.core.sql_engine import sync_engine
from src.domain.db.tipo_evento import TipoEvento


class TipoEventoRepository:
    def __init__(self) -> None:
        self.engine = sync_engine()

    def create_tipo_evento(self, tipo_evento: TipoEvento) -> TipoEvento:
        with Session(self.engine) as session:
            session.add(tipo_evento)
            session.commit()

        return tipo_evento

    def find_all_tipo_eventos(self) -> List:
        with Session(self.engine) as session:
            tipo_eventos = session.query(TipoEvento).all()

        return tipo_eventos

    def find_tipo_evento_by_id(self, id: int) -> Any:
        with Session(self.engine) as session:
            tipo_evento = session.query(TipoEvento).filter_by(id_tipo_evento=id).first()

        if not tipo_evento:
            raise Exception("No tipo evento found")

        return tipo_evento

    def update_tipo_evento(self, tipo_evento: TipoEvento, id: int) -> Any:
        with Session(self.engine) as session:
            new_tipo_evento = session.query(TipoEvento).filter_by(id_tipo_evento=id).first()

            if not new_tipo_evento:
                raise Exception("No tipo evento found")

            new_tipo_evento.descricao = tipo_evento.descricao

            session.commit()

        return new_tipo_evento

    def delete_tipo_evento_by_id(self, id: int) -> Any:
        with Session(self.engine) as session:
            tipo_evento = session.query(TipoEvento).filter_by(id_tipo_evento=id).first()

            if not tipo_evento:
                raise Exception("No tipo evento found")

            session.delete(tipo_evento)
            session.commit()
