from Estoque.ProdutoEstoque import Item
from src.TipoMedida import TipoMedida


class Leite(Item):
    CAPACIDADE_MAXIMA = 1000
    NOME = "leite"
    LIMITE_ALERTA = 200
    medida = TipoMedida.ML
