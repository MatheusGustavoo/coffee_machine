from src.Estoque.ProdutoEstoque import Item
from src.models.estoque import TipoMedida


class Acucar(Item):
    NOME = "acucar"
    CAPACIDADE_MAXIMA = 300
    LIMITE_ALERTA = 60
    medida = TipoMedida.G


Açúcar = Acucar
