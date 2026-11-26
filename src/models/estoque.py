import enum

from sqlalchemy import Enum
from sqlalchemy.orm import Mapped, mapped_column

from src.database.base import Base


class TipoMedida(enum.Enum):
    ML = "ml"
    UNIDADE = "unidade"
    G = "g"


class Estoque(Base):
    __tablename__ = "estoque"

    id: Mapped[int] = mapped_column(primary_key=True)
    item: Mapped[str] = mapped_column(unique=True)
    unidade: Mapped[TipoMedida] = mapped_column(Enum(TipoMedida))
    atual: Mapped[int]
    capacidade: Mapped[int]
    limite_alerta: Mapped[int]

