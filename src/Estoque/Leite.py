from src.Estoque.ProdutoEstoque import Item
from src.models.estoque import TipoMedida


class Leite(Item):
    CAPACIDADE_MAXIMA = 1000
    NOME = "leite"
    LIMITE_ALERTA = 200
    medida = TipoMedida.ML
