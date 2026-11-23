from Estoque.ProdutoEstoque import Item
from src.TipoMedida import TipoMedida


class CafeEmGraos(Item):
    CAPACIDADE_MAXIMA = 500
    NOME = "cafe"
    LIMITE_ALERTA = 100
    medida = TipoMedida.G


CaféEmGrãos = CafeEmGraos
CaféEmGraos = CafeEmGraos
