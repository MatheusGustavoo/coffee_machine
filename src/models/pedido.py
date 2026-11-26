import enum
from datetime import datetime
from decimal import Decimal

from sqlalchemy import Enum, ForeignKey, Numeric
from sqlalchemy.orm import Mapped, mapped_column

from src.database.base import Base

class StatusPedido(enum.Enum):
    EM_PREPARO = "EM_PREPARO"
    PRONTO = "PRONTO"
    CANCELADO = "CANCELADO"

class Pedido(Base):
    __tablename__ = "pedido"

    id: Mapped[int] = mapped_column(primary_key=True)
    produto_id: Mapped[int] = mapped_column(ForeignKey("produto.id"))
    acucar: Mapped[int]
    preco: Mapped[Decimal] = mapped_column(Numeric(10,2))
    status: Mapped[StatusPedido] = mapped_column(Enum(StatusPedido))
    criado_em: Mapped[datetime]
    previsao_termino: Mapped[datetime]

