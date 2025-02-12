from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from src.domain.db.base import Base


class Historico(Base):
    __tablename__ = "historico"

    id_historico: Mapped[int] = mapped_column(primary_key=True)

    id_solicitacao: Mapped[int] = mapped_column(nullable=False)
    usuario_responsavel: Mapped[int] = mapped_column(nullable=False)

    campo_modificado: Mapped[str] = mapped_column(String(100), nullable=False)

    valor_anterior: Mapped[str] = mapped_column(Text, nullable=False)
    valor_novo: Mapped[str] = mapped_column(Text, nullable=False)
