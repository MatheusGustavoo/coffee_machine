from dataclasses import replace

from src.Bebida import Bebida

CAFE_EXPRESSO = Bebida(
    nome="Café expresso",
    agua_ml=40,
    cafe_g=8,
    leite_ml=0,
    chocolate_g=0,
    acucar_g=0,
    preco=4.00,
)

CAFE_LONGO = Bebida(
    nome="Café longo",
    agua_ml=120,
    cafe_g=8,
    leite_ml=0,
    chocolate_g=0,
    acucar_g=0,
    preco=4.50,
)

CAFE_COM_LEITE = Bebida(
    nome="Café com leite",
    agua_ml=40,
    cafe_g=8,
    leite_ml=150,
    chocolate_g=0,
    acucar_g=00,
    preco=6.00,
)

CAPPUCCINO = Bebida(
    nome="Cappuccino",
    agua_ml=40,
    cafe_g=8,
    leite_ml=100,
    chocolate_g=5,
    acucar_g=0,
    preco=6.50,
)

CHOCOLATE_QUENTE = Bebida(
    nome="Chocolate quente",
    agua_ml=50,
    cafe_g=0,
    leite_ml=120,
    chocolate_g=30,
    acucar_g=0,
    preco=7.00,
)

CATALOGO = {
    bebida.nome: bebida
    for bebida in [
        CAFE_EXPRESSO,
        CAFE_LONGO,
        CAFE_COM_LEITE,
        CAPPUCCINO,
        CHOCOLATE_QUENTE,
    ]
}


class CatalogoBebidas:
    def __init__(self, bebidas: dict[str, Bebida]) -> None:
        self._bebidas = bebidas.copy()

    def buscar(self, nome: str) -> Bebida:
        chave = nome.strip().casefold()
        for bebida in self._bebidas.values():
            if bebida.nome.casefold() == chave:
                return bebida
        raise KeyError(f"Bebida não encontrada no catálogo: {nome}")

    def listar(self) -> tuple[Bebida, ...]:
        return tuple(self._bebidas.values())


class BebidaFactory:
    def __init__(self, catalogo: CatalogoBebidas) -> None:
        self._catalogo = catalogo

    def criar(self, nome: str, quantidade_acucar: float | None = None) -> Bebida:
        bebida = self._catalogo.buscar(nome)
        if quantidade_acucar is None:
            return replace(bebida)
        if quantidade_acucar < 0:
            raise ValueError("A quantidade de açúcar não pode ser negativa.")
        return replace(bebida, acucar_g=quantidade_acucar)


catalogo = CatalogoBebidas(CATALOGO)
fabrica_bebidas = BebidaFactory(catalogo)
