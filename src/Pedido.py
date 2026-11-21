import ItemInterface
import PedidoDTO


class Pedido:
    _valor_total: float
    _itens_pedido: list[ItemInterface]

    def __init__(self) -> None:
        self._itens_pedido = []
        self._valor_total = 0.0

    def incluir_item(self, itens_pedido: PedidoDTO):

        for item in itens_pedido.itens:
            self._itens_pedido.append(item)
            self._update_valor_total(item.get_valor(), "adicionar")

    def remover_item(self, item: ItemInterface):
        pass

    def get_valor_total(self) -> float:
        return self._valor_total

    def _update_valor_total(self, valor: float, operacao: str) -> None:
        if operacao == "adicionar":
            self._valor_total += valor
        elif operacao == "subtrair":
            self._valor_total -= valor
