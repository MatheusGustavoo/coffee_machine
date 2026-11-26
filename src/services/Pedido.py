from src.Catalogo.Bebida import Bebida
from src.Catalogo.CatalogoBebidas import fabrica_bebidas
from src.Estoque.Estoque import Estoque
from src.DTO.PedidoDTO import PedidoDTO
from src.models.pedido import StatusPedido


class Pedido:
    _valor_total: float
    _itens_pedido: list
    _estoque: Estoque
    _status: StatusPedido

    def __init__(self, estoque: Estoque) -> None:
        self._itens_pedido = []
        self._valor_total = 0.0
        self._estoque = estoque
        self._status = StatusPedido.EM_PREPARO
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
                self._verificar_status(StatusPedido.EM_PREPARO)
                self._status = StatusPedido.PRONTO
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

    def _verificar_status(self, esperado: StatusPedido) -> None:
        if self._status != esperado:
            raise ValueError(
                f"Status do pedido inválido. Esperado: {esperado.value}, Atual: {self._status.value}"
            )

    def set_status(self, novo_status: str) -> None:
        self._status = StatusPedido(novo_status)

    # def get_itens_pedido(self) -> list[ItemInterface]:
    #     return self._itens_pedido
