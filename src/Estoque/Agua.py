from src.Estoque.ProdutoEstoque import Item
from src.models.estoque import TipoMedida


class Agua(Item):
    CAPACIDADE_MAXIMA = 2000
    NOME = "agua"
    LIMITE_ALERTA = 400
    medida = TipoMedida.ML


Água = Agua
