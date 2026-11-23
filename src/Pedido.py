from Catalogo.Bebida import Bebida
from Catalogo.CatalogoBebidas import fabrica_bebidas
from Estoque.Estoque import Estoque
from PedidoDTO import PedidoDTO


class Pedido:
    _valor_total: float
    _itens_pedido: list
    _estoque: Estoque

    def __init__(self, estoque: Estoque) -> None:
        self._itens_pedido = []
        self._valor_total = 0.0
        self._estoque = estoque
        self._fabrica_bebidas = fabrica_bebidas

    def incluir_item(self, itens_pedido: PedidoDTO):
        for item in itens_pedido.itens:
            try:
                nome_produto = item.nome_item
                quantidade_acucar = item.quantidade_acucar
                bebida: Bebida = self._fabrica_bebidas.criar(
                    nome_produto, quantidade_acucar
                )
                self._estoque.decrementar_quantidade(bebida, 1)
                self._itens_pedido.append(bebida)
                self._update_valor_total(bebida.preco, "adicionar")
            except Exception as e:
                raise ValueError(f"Erro ao incluir item {item}: {e!s}")

    # def remover_item(self, item: ItemInterface):
    #     pass

    def get_valor_total(self) -> float:
        return self._valor_total

    def _update_valor_total(self, valor: float, operacao: str) -> None:
        if operacao == "adicionar":
            self._valor_total += valor
        elif operacao == "subtrair":
            self._valor_total -= valor

    # def get_itens_pedido(self) -> list[ItemInterface]:
    #     return self._itens_pedido
