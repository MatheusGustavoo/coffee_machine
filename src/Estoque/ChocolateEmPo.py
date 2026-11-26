from src.Estoque.ProdutoEstoque import ProdutoEstoque
from src.models.estoque import TipoMedida


class ChocolateEmPo(ProdutoEstoque):
    CAPACIDADE_MAXIMA = 400
    NOME = "chocolate"
    LIMITE_ALERTA = 80
    medida = TipoMedida.G


ChocolateEmPó = ChocolateEmPo
