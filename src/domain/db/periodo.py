from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column

from src.domain.db.base import Base


class Periodo(Base):
    __tablename__ = "periodo"

    id_periodo: Mapped[int] = mapped_column(primary_key=True)

    id_solicitacao: Mapped[int] = mapped_column(nullable=False)

    data_inicio: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    data_fim: Mapped[datetime] = mapped_column(DateTime, nullable=False)
