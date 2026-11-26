from src.Estoque.ProdutoEstoque import Item
from src.models.estoque import TipoMedida


class Copos(Item):
    CAPACIDADE_MAXIMA = 50
    NOME = "copo"
    LIMITE_ALERTA = 10
    medida = TipoMedida.UNIDADE


Copo = Copos
