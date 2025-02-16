from datetime import datetime

from sqlalchemy import String, Text, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.domain.db.base import Base
from src.domain.db.usuario import Usuario


class Historico(Base):
    __tablename__ = "historico"

    id_historico: Mapped[int] = mapped_column(primary_key=True)

    id_solicitacao: Mapped[int] = mapped_column(ForeignKey("solicitacao.id_solicitacao"), nullable=False)
    usuario_responsavel: Mapped[int] = mapped_column(ForeignKey("usuario.id_usuario"), nullable=False)

    campo_modificado: Mapped[str] = mapped_column(String(100), nullable=False)

    valor_anterior: Mapped[str] = mapped_column(Text, nullable=False)
    valor_novo: Mapped[str] = mapped_column(Text, nullable=False)
    data_modificacao: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.now())

    solicitacao: Mapped["Solicitacao"] = relationship(back_populates="historico")
    usuario: Mapped["Usuario"] = relationship(back_populates="historico")
