from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped

from src.domain.db.base import Base


class TipoEvento(Base):
    __tablename__ = "tipoevento"

    id_tipo_evento: Mapped[int] = mapped_column(primary_key=True)

    descricao: Mapped[str] = mapped_column(String(100), nullable=True, unique=True)
