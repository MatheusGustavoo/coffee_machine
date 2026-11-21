class CreditoInsuficienteError(Exception):
    """Indica que não há crédito suficiente para iniciar um pedido."""


class MaquinaIndisponivelError(Exception):
    """Indica que a máquina não está disponível para iniciar um pedido."""


class EstoqueVazioError(Exception):
    """Indica que não há produtos cadastrados no estoque."""


class ProdutoIndisponivelError(Exception):
    """Indica que um produto não possui unidades disponíveis no estoque."""
