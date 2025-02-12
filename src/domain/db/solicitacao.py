from datetime import datetime
from typing import List

from sqlalchemy import String, DateTime, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.domain.db.autorizacao import Autorizacao
from src.domain.db.base import Base
from src.domain.db.historico import Historico
from src.domain.db.periodo import Periodo


class Solicitacao(Base):
    __tablename__ = "solicitacao"

    id_solicitacao: Mapped[int] = mapped_column(primary_key=True)

    id_solicitante: Mapped[int] = mapped_column(ForeignKey("solicitante.id_solicitante"), nullable=False)
    id_usuario: Mapped[int] = mapped_column(ForeignKey("usuario.id_usuario"), nullable=False)
    id_espaco: Mapped[int] = mapped_column(ForeignKey("espacopublico.id_espaco"), nullable=False)
    id_tipo_evento: Mapped[int] = mapped_column(ForeignKey("tipoevento.id_tipo_evento"), nullable=False)

    status: Mapped[int] = mapped_column(String(20), nullable=False, default="pendente")

    data_solicitacao: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.now())

    periodo: Mapped[List[Periodo]] = relationship()
    autorizacao: Mapped[List[Autorizacao]] = relationship()
    historico: Mapped[List[Historico]] = relationship()
