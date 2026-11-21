from src.ProdutoEstoque import Item
from src.TipoMedida import TipoMedida


class Leite(Item):
    CAPACIDADE_MAXIMA = 1000
    CAPAXIDADE_MAXIMA = CAPACIDADE_MAXIMA
    LIMITE_ALERTA = 200
    medida = TipoMedida.ML
