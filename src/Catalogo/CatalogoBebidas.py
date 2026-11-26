from dataclasses import replace

from src.Catalogo.Bebida import Bebida

CAFE_EXPRESSO = Bebida(
    nome="Café expresso",
    agua=40,
    cafe=8,
    leite=0,
    chocolate=0,
    preco=4.00,
)

CAFE_LONGO = Bebida(
    nome="Café longo",
    agua=120,
    cafe=8,
    leite=0,
    chocolate=0,
    preco=4.50,
)

CAFE_COM_LEITE = Bebida(
    nome="Café com leite",
    agua=40,
    cafe=8,
    leite=150,
    chocolate=0,
    preco=6.00,
)

CAPPUCCINO = Bebida(
    nome="Cappuccino",
    agua=40,
    cafe=8,
    leite=100,
    chocolate=5,
    preco=6.50,
)

CHOCOLATE_QUENTE = Bebida(
    nome="Chocolate quente",
    agua=50,
    cafe=0,
    leite=120,
    chocolate=30,
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

    def alterar_preco(self, nome: str, novo_preco: float) -> None:
        if novo_preco < 0:
            raise ValueError("O preço não pode ser negativo.")
        bebida = self.buscar(nome)
        bebida.preco = novo_preco


class BebidaFactory:
    def __init__(self, catalogo: CatalogoBebidas) -> None:
        self._catalogo = catalogo

    def criar(self, nome: str, quantidade_acucar: float | None = None) -> Bebida:
        bebida = self._catalogo.buscar(nome)
        if quantidade_acucar is None:
            return replace(bebida)
        if quantidade_acucar < 0:
            raise ValueError("A quantidade de açúcar não pode ser negativa.")
        return replace(bebida, acucar=quantidade_acucar)


catalogo = CatalogoBebidas(CATALOGO)
fabrica_bebidas = BebidaFactory(catalogo)
