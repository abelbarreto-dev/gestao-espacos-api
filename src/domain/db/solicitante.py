from typing import List

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.domain.db.base import Base


class Solicitante(Base):
    __tablename__ = "solicitante"

    id_solicitante: Mapped[int] = mapped_column(primary_key=True)

    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    tipo: Mapped[str] = mapped_column(String(20), nullable=False)
    documento: Mapped[str] = mapped_column(String(20), nullable=False, unique=True)
    contato: Mapped[str] = mapped_column(String(50), nullable=False)

    solicitacao: Mapped[List["Solicitacao"]] = relationship(back_populates="solicitante", cascade="all, delete-orphan")
