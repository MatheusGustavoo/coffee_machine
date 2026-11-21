from src.Bebida import Bebida

CAFE_EXPRESSO = Bebida(
    nome="Café expresso",
    agua_ml=40,
    cafe_g=8,
    leite_ml=0,
    chocolate_g=0,
    acucar_g=5,
    preco=4.00,
)

CAFE_LONGO = Bebida(
    nome="Café longo",
    agua_ml=120,
    cafe_g=8,
    leite_ml=0,
    chocolate_g=0,
    acucar_g=8,
    preco=4.50,
)

CAFE_COM_LEITE = Bebida(
    nome="Café com leite",
    agua_ml=40,
    cafe_g=8,
    leite_ml=150,
    chocolate_g=0,
    acucar_g=10,
    preco=6.00,
)

CAPPUCCINO = Bebida(
    nome="Cappuccino",
    agua_ml=40,
    cafe_g=8,
    leite_ml=100,
    chocolate_g=5,
    acucar_g=12,
    preco=6.50,
)

CHOCOLATE_QUENTE = Bebida(
    nome="Chocolate quente",
    agua_ml=50,
    cafe_g=0,
    leite_ml=120,
    chocolate_g=30,
    acucar_g=12,
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
