import enum

from src.Credito import Credito, Valores
from src.Estoque import Estoque
from src.Excessoes import (
    CreditoInsuficienteError,
    EstoqueVazioError,
    MaquinaIndisponivelError,
    ProdutoIndisponivelError,
)
from src.Pedido import Pedido


class Estado_Maquina(enum.Enum):
    PRONTA = "aceita crédito e pedidos"
    AGUARDANDO_LIMPEZA = (
        "atingido o limite de 30 preparos desde a última limpeza; pedidos bloqueados."
    )
    MANUTENCAO = (
        "colocada pelo operador para reabastecer ou limpar; pedidos bloqueados."
    )
    PREPARANDO = "há uma bebida em preparo; novos pedidos são recusados até o término."


class Maquina:
    _estado: Estado_Maquina
    _credito: Credito
    _estoque: Estoque

    def __init__(self) -> None:
        self.set_estado(Estado_Maquina.PRONTA)
        self._credito = Credito()
        self._estoque = Estoque()
        print(
            f"Máquina inicializada. Estado: {self._estado.value}. "
            f"Crédito: R${self._credito.disponivel:.2f}"
        )

    def realizar_pedido(self):
        if self._estado != Estado_Maquina.PRONTA:
            raise MaquinaIndisponivelError(
                f"A máquina não está disponível para iniciar um pedido. Estado atual: {self._estado.value}"
            )
        try:
            pedido = Pedido(status_maquina=self._estado)
            self._verificar_elegibilidade_do_pedido(pedido)
            self.set_estado(Estado_Maquina.PREPARANDO)
            return "Pedido iniciado. A máquina está preparando a bebida."
        except Exception as e:
            return str(e)

    def _verificar_elegibilidade_do_pedido(self, pedido: Pedido) -> None:
        if self._credito.disponivel < pedido.get_valor_total():
            raise CreditoInsuficienteError(
                "Crédito insuficiente. Por favor, insira crédito antes de iniciar um pedido."
            )

        elif self._estoque.vazio():
            raise EstoqueVazioError(
                "Estoque vazio. Por favor, reabasteça o estoque antes de iniciar um pedido."
            )
        for produto in self._estoque.listar_produtos():
            if produto.get_quantidade() <= 0:
                raise ProdutoIndisponivelError(
                    f"Produto {produto} indisponível. Por favor, reabasteça o estoque."
                )

    def set_estado(self, estado: Estado_Maquina) -> None:
        self._estado = estado
        print(f"Estado da máquina alterado para: {self._estado.value}")

    def inserir_credito(self, valor: float | int) -> None:
        valor_tipado = Valores.de_valor(valor)
        self._credito.inserir_valor(valor_tipado)
        print(
            f"Crédito inserido: R${valor_tipado.value:.2f}. "
            f"Crédito disponível: R${self._credito.disponivel:.2f}"
        )
