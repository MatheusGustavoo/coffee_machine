from src.ProdutoEstoque import Item
from src.TipoMedida import TipoMedida


class ChocolateEmPo(Item):
    CAPACIDADE_MAXIMA = 400
    CAPAXIDADE_MAXIMA = CAPACIDADE_MAXIMA
    LIMITE_ALERTA = 80
    medida = TipoMedida.G


ChocolateEmPó = ChocolateEmPo
