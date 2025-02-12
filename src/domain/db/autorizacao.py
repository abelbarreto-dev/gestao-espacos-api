from datetime import date

from sqlalchemy import Integer, Date
from sqlalchemy.orm import Mapped, mapped_column

from src.domain.db.base import Base


class Autorizacao(Base):
    __tablename__ = "autorizacao"

    id_autorizacao: Mapped[int] = mapped_column(primary_key=True)

    id_solicitacao: Mapped[int] = mapped_column(Integer, nullable=False, unique=True)

    data_emissao: Mapped[date] = mapped_column(Date, nullable=False, dafault=date.today())
    validade: Mapped[date] = mapped_column(Date, nullable=False)
