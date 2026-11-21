from Estoque.ProdutoEstoque import ProdutoEstoque
from src.TipoMedida import TipoMedida


class ChocolateEmPo(ProdutoEstoque):
    CAPACIDADE_MAXIMA = 400
    LIMITE_ALERTA = 80
    medida = TipoMedida.G


ChocolateEmPó = ChocolateEmPo
