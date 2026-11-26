import enum

from src.Estoque.Estoque import Estoque
from src.Excessoes.Excessoes import (
    MaquinaIndisponivelError,
)
from src.services.Credito import Credito, Valores
from src.services.Pedido import Pedido
from src.DTO.PedidoDTO import PedidoDTO


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
    _pedido_atual: Pedido | None

    def __init__(self) -> None:
        self._preparo_desde_limpeza = 0
        self.set_estado(Estado_Maquina.PRONTA)
        self._credito = Credito()
        self._estoque = Estoque()
        print(
            f"Máquina inicializada. Estado: {self._estado.value}. "
            f"Crédito: R${self._credito.disponivel:.2f}"
        )

    def criar_pedido(self, itens_pedido: PedidoDTO):
        if self._estado != Estado_Maquina.PRONTA:
            raise MaquinaIndisponivelError(
                f"A máquina não está disponível para iniciar um pedido. Estado atual: {self._estado.value}"
            )
        try:
            pedido = Pedido(self._estoque)
            self._pedido_atual = pedido
            self.set_estado(Estado_Maquina.PREPARANDO)
            pedido.incluir_item(itens_pedido)
            self._credito.retirar_valor(pedido.get_valor_total())

            self.registrar_preparo_concluido()
            
        except Exception as e:
            return str(e)
        finally:
            if self._estado != Estado_Maquina.AGUARDANDO_LIMPEZA:
                self.set_estado(Estado_Maquina.PRONTA)

    def set_estado(self, estado: Estado_Maquina) -> None:
        self._estado = estado
        print(f"Estado da máquina alterado para: {self._estado.value}")

    def inserir_credito(self, valor: float) -> None:
        valor_tipado = Valores.de_valor(valor)
        self._credito.inserir_valor(valor_tipado)
        print(
            f"Crédito inserido: R${valor_tipado.value:.2f}. "
            f"Crédito disponível: R${self._credito.disponivel:.2f}"
        )

    def cancelar_pedido(self, id):
        if self._estado != Estado_Maquina.PREPARANDO:
            raise MaquinaIndisponivelError(
                f"A máquina não está preparando um pedido. Estado atual: {self._estado.value}"
            )

        if self._pedido_atual is None:
            raise ValueError("Não há pedido em andamento para cancelar.")

        try:
            self._pedido_atual.set_status("CANCELADO")
            self._pedido_atual = None
            self.set_estado(Estado_Maquina.PRONTA)
            print("Pedido cancelado. Reembolsando crédito.")
        except Exception as e:
            raise ValueError(f"Erro ao cancelar pedido: {e!s}")

    def devolver_credito(self) -> None:
        self._credito.zerar()
        print(f"Crédito devolvido: R${self._credito.disponivel:.2f}")

    def registrar_preparo_concluido(self) -> None:
        self.preparo_desde_limpeza += 1
        if self.preparo_desde_limpeza >= 30:
            self.set_estado(Estado_Maquina.AGUARDANDO_LIMPEZA)

    def registrar_limpeza(self) -> None:
        self._preparo_desde_limpeza = 0