from sqlalchemy import String, Text, Boolean, Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from src.domain.db.base import Base


class EspacoPublico(Base):
    __tablename__ = "espacopublico"

    id_espaco: Mapped[int] = mapped_column(primary_key=True)

    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    endereco: Mapped[Text] = mapped_column(String(255), nullable=False)
    descricao: Mapped[str] = mapped_column(Text, nullable=True)
    capacidade: Mapped[int] = mapped_column(Integer, nullable=False)
    disponibilidade: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
