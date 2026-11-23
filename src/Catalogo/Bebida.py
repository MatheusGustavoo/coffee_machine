from dataclasses import dataclass


@dataclass
class Bebida:
    nome: str
    agua: float
    cafe: float
    leite: float
    preco: float
    chocolate: float
    acucar: float | None = 0
    copo: int | None = 1
