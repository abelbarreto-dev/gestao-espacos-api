from typing import List

from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column

from src.domain.db.base import Base
from src.domain.db.historico import Historico
from src.domain.db.solicitacao import Solicitacao


class Usuario(Base):
    __tablename__ = "usuario"

    id_usuario: Mapped[int] = mapped_column(primary_key=True)

    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    senha: Mapped[str] = mapped_column(Text, nullable=False)
    perfil: Mapped[str] = mapped_column(String(20), nullable=False)

    solicitacao: Mapped[List[Solicitacao]] = relationship()
    historico: Mapped[List[Historico]] = relationship()
