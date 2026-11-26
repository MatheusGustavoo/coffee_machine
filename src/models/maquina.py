import enum
from decimal import Decimal

from sqlalchemy import Enum, Numeric
from sqlalchemy.orm import Mapped, mapped_column

from src.database.base import Base


class EstadoMaquina(enum.Enum):
    PRONTA = "PRONTA"
    PREPARANDO = "PREPARANDO"
    AGUARDANDO_LIMPEZA = "AGUARDANDO_LIMPEZA"
    MANUTENCAO = "MANUTENCAO"


class Maquina(Base):
    __tablename__ = "maquina"

    id: Mapped[int] = mapped_column(primary_key=True)
    estado: Mapped[EstadoMaquina] = mapped_column(Enum(EstadoMaquina))
    credito: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    preparos_desde_limpeza: Mapped[int]

