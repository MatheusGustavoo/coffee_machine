from src.ProdutoEstoque import Item
from src.TipoMedida import TipoMedida


class Copos(Item):
    CAPACIDADE_MAXIMA = 50
    CAPAXIDADE_MAXIMA = CAPACIDADE_MAXIMA
    LIMITE_ALERTA = 10
    medida = TipoMedida.UNIDADE


Copo = Copos
