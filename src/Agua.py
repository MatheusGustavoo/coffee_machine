from src.ProdutoEstoque import Item
from src.TipoMedida import TipoMedida


class Agua(Item):
    CAPACIDADE_MAXIMA = 2000
    CAPAXIDADE_MAXIMA = CAPACIDADE_MAXIMA
    LIMITE_ALERTA = 400
    medida = TipoMedida.ML


Água = Agua
