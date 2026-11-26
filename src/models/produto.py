from decimal import Decimal

from sqlalchemy import Numeric
from sqlalchemy.orm import Mapped, mapped_column

from src.database.base import Base

class Produto(Base):
    __tablename__ = "produto" 

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(unique=True)
    preco: Mapped[Decimal] = mapped_column(Numeric(10,2))
    tempo_preparo_s: Mapped[int]
    agua_ml: Mapped[int]
    cafe_g: Mapped[int]
    leite_ml: Mapped[int]
    chocolate_g: Mapped[int]