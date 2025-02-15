from typing import List

from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.domain.db.base import Base
from src.domain.db.solicitacao import Solicitacao


class TipoEvento(Base):
    __tablename__ = "tipoevento"

    id_tipo_evento: Mapped[int] = mapped_column(primary_key=True)

    descricao: Mapped[str] = mapped_column(String(100), nullable=True, unique=True)

    solicitacao: Mapped[List["Solicitacao"]] = relationship(back_populates="tipoevento", cascade="all, delete-orphan")
