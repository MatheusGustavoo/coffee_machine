from src.ProdutoEstoque import Item
from src.TipoMedida import TipoMedida


class Acucar(Item):
    CAPACIDADE_MAXIMA = 300
    CAPAXIDADE_MAXIMA = CAPACIDADE_MAXIMA
    LIMITE_ALERTA = 60
    medida = TipoMedida.G


Açúcar = Acucar
