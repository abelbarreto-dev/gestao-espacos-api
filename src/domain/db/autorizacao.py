from datetime import date

from sqlalchemy import ForeignKey, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.domain.db.base import Base


class Autorizacao(Base):
    __tablename__ = "autorizacao"

    id_autorizacao: Mapped[int] = mapped_column(primary_key=True)

    id_solicitacao: Mapped[int] = mapped_column(ForeignKey("solicitacao.id_solicitacao"), nullable=False, unique=True)

    data_emissao: Mapped[date] = mapped_column(Date, nullable=False, default=date.today())
    validade: Mapped[date] = mapped_column(Date, nullable=False)

    solicitacao: Mapped["Solicitacao"] = relationship(back_populates="autorizacao")
