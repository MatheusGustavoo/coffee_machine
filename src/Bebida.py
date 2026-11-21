from dataclasses import dataclass


@dataclass
class Bebida:
    nome: str
    agua_ml: float
    cafe_g: float
    leite_ml: float
    preco: float
    chocolate_g: float
    acucar_g: float
    quantidade_acucar: float | None = None
