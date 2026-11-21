from Estoque.ProdutoEstoque import Item
from src.TipoMedida import TipoMedida


class Agua(Item):
    CAPACIDADE_MAXIMA = 2000
    LIMITE_ALERTA = 400
    medida = TipoMedida.ML


Água = Agua
